#!/usr/bin/env python3
"""
Build docs/<topic>/<CODE>.md from three sources:

  data/raw/<CODE>.json    problem payload fetched from CodeChef
  data/authored/<CODE>.md hand written front matter + "Approach" prose
  solutions/<CODE>.py     the runnable Python solution

Writes two views of the same content:

  docs/<topic>/<CODE>.md        grouped by topic
  by-rating/<NNNN>-<CODE>.md    ordered by CodeChef difficulty rating

Also regenerates README.md and by-rating/README.md.
"""
import html, json, os, re, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import complexity as X
import constraints as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'data', 'raw')
AUTH = os.path.join(ROOT, 'data', 'authored')
SOLN = os.path.join(ROOT, 'solutions')
DOCS = os.path.join(ROOT, 'docs')
RATED = os.path.join(ROOT, 'by-rating')
BYCPX = os.path.join(ROOT, 'by-complexity')

META = json.load(open(os.path.join(ROOT, 'data', 'problem_meta.json')))
IDX = json.load(open(os.path.join(ROOT, 'data', 'roadmap_index.json')))

HTMLISH = re.compile(r'</?(?:p|b|i|u|ul|ol|li|h[1-6]|pre|div|br|strong|em|sub|sup|center|table|tr|td)\b[^>]*>', re.I)


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def parse_authored(path):
    """Front matter, the approach prose, and any extra `## Name` sections."""
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', text, flags=re.S)
    if not m:
        raise ValueError(f'{path}: missing front matter')
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        k, _, v = line.partition(':')
        meta[k.strip()] = v.strip()
    parts = re.split(r'^## +(.+?)\s*$', m.group(2), flags=re.M)
    sections = {parts[i].strip().lower(): parts[i + 1].strip()
                for i in range(1, len(parts) - 1, 2)}
    return meta, parts[0].strip(), sections


def html_to_md(h):
    """Older problems store the statement as HTML. Strip only recognised tags
    so bare comparisons such as `1 <= N <= 100` survive."""
    h = re.sub(r'<aside.*?</aside>', '', h, flags=re.S | re.I)
    h = re.sub(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', r'[\2](\1)', h, flags=re.S | re.I)
    h = re.sub(r'<(?:b|strong)\b[^>]*>(.*?)</(?:b|strong)>', r'**\1**', h, flags=re.S | re.I)
    h = re.sub(r'<(?:i|em)\b[^>]*>(.*?)</(?:i|em)>', r'*\1*', h, flags=re.S | re.I)
    h = re.sub(r'<sub\b[^>]*>(.*?)</sub>', r'_\1', h, flags=re.S | re.I)
    h = re.sub(r'<sup\b[^>]*>(.*?)</sup>', r'^\1', h, flags=re.S | re.I)
    h = re.sub(r'<pre\b[^>]*>(.*?)</pre>',
               lambda m: '\n```\n' + m.group(1).strip() + '\n```\n', h, flags=re.S | re.I)
    h = re.sub(r'<h[1-6]\b[^>]*>(.*?)</h[1-6]>', r'\n\n**\1**\n', h, flags=re.S | re.I)
    h = re.sub(r'<br\s*/?>', '\n', h, flags=re.I)
    h = re.sub(r'<li\b[^>]*>', '- ', h, flags=re.I)
    h = re.sub(r'</(?:p|li|ul|ol|h[1-6]|div)>', '\n', h, flags=re.I)
    return html.unescape(HTMLISH.sub('', h))


def clean(md):
    if not md:
        return ''
    md = md.replace('\r\n', '\n').replace('\r', '\n')
    if HTMLISH.search(md):
        md = html_to_md(md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    return re.sub(r'\n{3,}', '\n\n', md).strip()


def fence(text):
    text = (text or '').replace('\r\n', '\n').rstrip()
    bt = '```'
    while bt in text:
        bt += '`'
    return f'{bt}\n{text}\n{bt}'


# `user_tags` mixes real topic labels with setter handles ("satyam_adm",
# "notsoloud") and contest codes ("start111", "may13"), so they are filtered.
TAG_STOP = {'admin', 'easy', 'medium', 'hard', 'simple', 'cakewalk', 'challenge',
            'peer', 'tutorial', 'easy-medium', 'medium-hard', 'easy-tutorial'}
TAG_NOISE = re.compile(r'_adm$|^[a-z][a-z_]*\d+[a-z]?$|\d{2,}')


# Enumerating the all-lowercase single-word tags left only 16 candidates, of
# which these five are topics; the rest were setter handles or difficulty words.
TAG_PLAIN_OK = {'math', 'maths', 'geometry', 'greedy', 'sorting'}


def topic_tag(t):
    """Keep Title-Cased labels, hyphenated lowercase ones, and the vetted
    lowercase words; drop setter handles, contest codes and difficulty words."""
    s = (t or '').strip()
    if not s or s.lower() in TAG_STOP or TAG_NOISE.search(s.lower()):
        return False
    if s.lower() in TAG_PLAIN_OK:
        return True
    return any(ch.isupper() for ch in s) or ('-' in s and s.islower())


def chef_tags(raw):
    """CodeChef's own labels: curated categories first, then vetted user tags."""
    out = []
    for group in (raw.get('computed_tags') or [], raw.get('user_tags') or []):
        for t in group:
            if t and t not in out and topic_tag(t):
                out.append(t)
    return out


def load(code):
    raw = json.load(open(os.path.join(RAW, f'{code}.json'), encoding='utf-8'))
    meta, approach, sections = parse_authored(os.path.join(AUTH, f'{code}.md'))
    solution = open(os.path.join(SOLN, f'{code}.py'), encoding='utf-8').read().rstrip()
    pm = META[code]
    pc = raw.get('problemComponents') or {}
    cons = clean(C.resolve(raw, code))
    if not cons:
        print(f'  !! {code}: no constraints', file=sys.stderr)
    rating = raw.get('difficulty_rating')
    rating = int(rating) if str(rating).lstrip('-').isdigit() else -1
    return {
        'code': code, 'raw': raw, 'pc': pc, 'meta': meta, 'approach': approach,
        'solution': solution, 'pm': pm, 'cons': cons,
        'sections': sections,
        'name': raw.get('problem_name') or code,
        'rating': rating,
        'timelimit': raw.get('max_timelimit') or '?',
        # Modern problems keep the prose in `statement`; legacy ones only in `body`.
        'statement': clean(pc.get('statement')) or clean(raw.get('body')),
        'tags': chef_tags(raw),
        'best_tag': raw.get('best_tag') or '',
        'category': raw.get('category_name') or '',
    }


def rated_name(d):
    """0000-padded rating prefix so a plain listing is in difficulty order."""
    if d['rating'] <= 0:
        return f'unrated-{d["code"]}.md'
    return f'{d["rating"]:04d}-{d["code"]}.md'


def problem_body(d, A):
    """Question, constraints and samples - shared by both views."""
    pc = d['pc']
    A('## Question\n')
    A(d['statement'] + '\n')
    if clean(pc.get('inputFormat')):
        A('**Input**\n')
        A(clean(pc.get('inputFormat')) + '\n')
    if clean(pc.get('outputFormat')):
        A('**Output**\n')
        A(clean(pc.get('outputFormat')) + '\n')
    A('## Constraints\n')
    A((d['cons'] or '_Not published for this problem._') + '\n')
    if clean(pc.get('subtasks')):
        A('**Subtasks**\n')
        A(clean(pc.get('subtasks')) + '\n')
    samples = pc.get('sampleTestCases') or []
    if samples:
        A('## Sample\n')
        for i, s in enumerate(samples, 1):
            label = f'Sample {i}' if len(samples) > 1 else 'Sample'
            A(f'**{label} input**\n')
            A(fence(s.get('input')) + '\n')
            A(f'**{label} output**\n')
            A(fence(s.get('output')) + '\n')
            if clean(s.get('explanation')):
                A('<details><summary>Explanation</summary>\n')
                A(clean(s.get('explanation')) + '\n')
                A('</details>\n')


def solution_body(d, A):
    """Approach, code and complexity - shared by both views."""
    meta = d['meta']
    A('## Approach\n')
    A(d['approach'] + '\n')
    A('## Solution (Python)\n')
    A('```python')
    A(d['solution'])
    A('```\n')
    A('## Complexity\n')
    A(f'- **Time:** {meta["time"]}')
    A(f'- **Space:** {meta["space"]}')
    if meta.get('complexity_note'):
        A(f'- {meta["complexity_note"]}')
    A('')


def render_rated(d):
    """The by-rating view: difficulty first, then the topics used."""
    meta, pm = d['meta'], d['pm']
    rating = d['rating'] if d['rating'] > 0 else 'unrated'
    P = []
    A = P.append
    A(f'# {rating} &middot; {d["name"]}\n')
    A(f'> CodeChef problem code [`{d["code"]}`]'
      f'(https://www.codechef.com/problems/{d["code"]}) &middot; '
      f'time limit **{d["timelimit"]}s** &middot; '
      f'{pm["course_title"]} (Level {pm["level"]})\n')
    A('## Topics used\n')
    A('| | |')
    A('|---|---|')
    A(f'| **Topic** | {meta["topic"]} |')
    A(f'| **Technique** | {meta.get("subtopic", "-")} |')
    if d['tags']:
        A(f'| **CodeChef tags** | {", ".join(f"`{t}`" for t in d["tags"])} |')
    if d['best_tag']:
        A(f'| **CodeChef top tag** | `{d["best_tag"]}` |')
    if d['category']:
        A(f'| **CodeChef category** | {d["category"]} |')
    A(f'| **Time** | {meta["time"]} |')
    A(f'| **Space** | {meta["space"]} |')
    A('')
    topic_path = os.path.join('..', 'docs', slugify(meta['topic']), f'{d["code"]}.md')
    A(f'Same write-up grouped by topic: [{topic_path}]({topic_path})\n')
    problem_body(d, A)
    solution_body(d, A)
    return '\n'.join(P).rstrip() + '\n'


def render_complexity(d, seq):
    """The by-complexity view: the six sections asked for, in order."""
    meta, pm, sec = d['meta'], d['pm'], d['sections']
    key, note = X.classify(meta['time'])
    rating = d['rating'] if d['rating'] > 0 else 'unrated'
    P = []
    A = P.append
    A(f'# {seq:03d}. {d["name"]}\n')
    A(f'> [`{d["code"]}`](https://www.codechef.com/problems/{d["code"]}) '
      f'&middot; difficulty **{rating}** '
      f'&middot; complexity class **{X.LABEL[key]}** {X.CANON[key]}'
      f'{" (" + note + ")" if note else ""}\n')

    A('## Topic used\n')
    A('| | |')
    A('|---|---|')
    A(f'| **Topic** | {meta["topic"]} |')
    A(f'| **Technique** | {meta.get("subtopic", "-")} |')
    if d['tags']:
        A(f'| **CodeChef tags** | {", ".join(f"`{t}`" for t in d["tags"])} |')
    A(f'| **Time** | {meta["time"]} |')
    A(f'| **Space** | {meta["space"]} |')
    A('')

    A('## Problem\n')
    A(d['statement'] + '\n')

    A('## Problem constraints\n')
    A((d['cons'] or '_Not published for this problem._') + '\n')

    A('## Approach\n')
    A(d['approach'] + '\n')

    A('## Solution\n')
    A('```python')
    A(d['solution'])
    A('```\n')

    A('## Edge cases\n')
    A(sec['edge cases'] + '\n')

    A('## Dry run\n')
    A(sec['dry run'] + '\n')

    rel = os.path.join('..', 'docs', slugify(meta['topic']), f'{d["code"]}.md')
    A(f'---\n')
    A(f'Same problem grouped by topic: [{rel}]({rel})\n')
    return '\n'.join(P).rstrip() + '\n'


def complexity_order(codes):
    """seq number per code: cheapest class first, then easiest rating."""
    rows = []
    for c in codes:
        key, _ = X.classify(X.time_of(c))
        raw = json.load(open(os.path.join(RAW, f'{c}.json'), encoding='utf-8'))
        r = raw.get('difficulty_rating')
        r = int(r) if str(r).lstrip('-').isdigit() else -1
        rows.append((X.RANK[key], r if r > 0 else 10 ** 6, c, key))
    rows.sort()
    return {c: (i + 1, key) for i, (_, _, c, key) in enumerate(rows)}


def write_complexity_index(rows, order):
    """by-complexity/README.md, grouped by class in increasing cost."""
    done = {r['code'] for r in rows}
    by_class = defaultdict(list)
    for code, (seq, key) in order.items():
        by_class[key].append((seq, code))
    L = []
    A = L.append
    A('# Problems in order of complexity\n')
    A('Every problem ordered by the time complexity of its solution, cheapest '
      'first, and numbered so a plain directory listing follows that order. '
      'Each file carries the topic used, the problem constraints, the '
      'approach, the solution, its edge cases and a dry run.\n')
    A('How a problem lands in a class is set out in `tools/complexity.py`: the '
      'class is the cost of **one test case** in the bounds the problem '
      'states, so a cost quoted per query or per item is multiplied up, and a '
      'one-off sieve is flagged rather than counted.\n')
    A(f'**{len(done)} of {len(order)} written.**\n')
    A('| # | Class | Problems | Written |')
    A('|---|---|---:|---:|')
    for rank, key, canon, label in X.CLASSES:
        rows_k = by_class.get(key, [])
        if not rows_k:
            continue
        n = sum(1 for _, c in rows_k if c in done)
        A(f'| {rank} | [{label} {canon}](#{rank}-{slugify(label)}) '
          f'| {len(rows_k)} | {n} |')
    A('')
    meta_by_code = {r['code']: r for r in rows}
    for rank, key, canon, label in X.CLASSES:
        rows_k = sorted(by_class.get(key, []))
        if not rows_k:
            continue
        A(f'## {rank}. {label}\n')
        A(f'{canon} &mdash; {len(rows_k)} problems\n')
        A('| # | Problem | Difficulty | Topic | Technique |')
        A('|---:|---|---:|---|---|')
        for seq, code in rows_k:
            r = meta_by_code.get(code)
            if r is None:
                A(f'| {seq:03d} | `{code}` _(not written yet)_ | | | |')
                continue
            shown = r['num_rating'] if r['num_rating'] > 0 else '&ndash;'
            A(f'| {seq:03d} | [{r["name"]}]({seq:03d}-{code}.md) `{code}` '
              f'| {shown} | {r["topic"]} | {r["subtopic"]} |')
        A('')
    A('---\n')
    A('Generated by `python3 tools/build_docs.py`.\n')
    os.makedirs(BYCPX, exist_ok=True)
    with open(os.path.join(BYCPX, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L).rstrip() + '\n')


def build_one(code):
    d = load(code)
    raw, meta, pm = d['raw'], d['meta'], d['pm']
    name, tl = d['name'], d['timelimit']
    rating = d['rating'] if d['rating'] > 0 else 'unrated'
    pc, cons, statement = d['pc'], d['cons'], d['statement']
    solution, approach = d['solution'], d['approach']

    topic = meta['topic']
    P = []
    A = P.append
    A(f'# {pm["order"]}. {name}\n')
    A(f'> CodeChef problem code [`{code}`]'
      f'(https://www.codechef.com/problems/{code}) &middot; '
      f'difficulty **{rating}** &middot; time limit **{tl}s**\n')
    A('| | |')
    A('|---|---|')
    A(f'| **Topic** | {topic} |')
    A(f'| **Technique** | {meta.get("subtopic", "-")} |')
    A(f'| **Time** | {meta["time"]} |')
    A(f'| **Space** | {meta["space"]} |')
    A(f'| **Roadmap course** | {pm["course_title"]} (Level {pm["level"]}) |')
    A('')
    problem_body(d, A)
    solution_body(d, A)
    tags = [t for t in (raw.get('computed_tags') or []) if t]
    if tags:
        A(f'> CodeChef tags: {", ".join(f"`{t}`" for t in tags)}\n')

    out_dir = os.path.join(DOCS, slugify(topic))
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f'{code}.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(P).rstrip() + '\n')

    seq = CPX_ORDER[code][0] if code in CPX_ORDER else None
    if seq and {'edge cases', 'dry run'} <= set(d['sections']):
        os.makedirs(BYCPX, exist_ok=True)
        with open(os.path.join(BYCPX, f'{seq:03d}-{code}.md'),
                  'w', encoding='utf-8') as f:
            f.write(render_complexity(d, seq))

    os.makedirs(RATED, exist_ok=True)
    rated_path = os.path.join(RATED, rated_name(d))
    with open(rated_path, 'w', encoding='utf-8') as f:
        f.write(render_rated(d))

    return {'code': code, 'name': name, 'rating': rating, 'topic': topic,
            'subtopic': meta.get('subtopic', '-'), 'order': pm['order'],
            'level': pm['level'], 'path': os.path.relpath(out_path, ROOT),
            'time': meta['time'], 'num_rating': d['rating'],
            'rated_file': rated_name(d), 'tags': d['tags'],
            'best_tag': d['best_tag'],
            'has_extras': {'edge cases', 'dry run'} <= set(d['sections'])}


BAND = 200


def write_rating_index(built):
    """by-rating/README.md: every problem in difficulty order, with its topics."""
    rated = sorted((b for b in built if b['num_rating'] > 0),
                   key=lambda b: (b['num_rating'], b['code']))
    unrated = sorted((b for b in built if b['num_rating'] <= 0),
                     key=lambda b: b['code'])
    bands = defaultdict(list)
    for b in rated:
        bands[b['num_rating'] // BAND * BAND].append(b)

    L = []
    A = L.append
    A('# Problems in difficulty order\n')
    A('The same write-ups as [`docs/`](../docs), ordered by CodeChef difficulty '
      'rating instead of grouped by topic, so they can be worked through from '
      'easiest to hardest. Each file names the topic and the technique it uses, '
      "alongside CodeChef's own tags.\n")
    A('Files are named `<rating>-<CODE>.md` with the rating zero-padded to four '
      'digits, so a plain directory listing is already in difficulty order. '
      'Problems CodeChef has not rated are named `unrated-<CODE>.md`.\n')
    A(f'**{len(built)} problems** &middot; ratings '
      f'{rated[0]["num_rating"]} to {rated[-1]["num_rating"]}'
      f'{f" &middot; {len(unrated)} unrated" if unrated else ""}\n')

    A('## Bands\n')
    A('| Band | Problems | Most common topic |')
    A('|---|---:|---|')
    for lo in sorted(bands):
        rows = bands[lo]
        top = Counter(r['topic'] for r in rows).most_common(1)[0]
        anchor = f'#{lo}{lo + BAND - 1}'
        A(f'| [{lo}&ndash;{lo + BAND - 1}]({anchor}) | {len(rows)} '
          f'| {top[0]} ({top[1]}) |')
    if unrated:
        top = Counter(r['topic'] for r in unrated).most_common(1)[0]
        A(f'| [Unrated](#unrated) | {len(unrated)} | {top[0]} ({top[1]}) |')
    A('')

    def table(rows):
        A('| Rating | Problem | Topic | Technique | CodeChef tags |')
        A('|---:|---|---|---|---|')
        for r in rows:
            shown = r['num_rating'] if r['num_rating'] > 0 else '&ndash;'
            tags = ', '.join(f'`{t}`' for t in r['tags'][:4]) or '&ndash;'
            A(f'| {shown} | [{r["name"]}]({r["rated_file"]}) `{r["code"]}` '
              f'| {r["topic"]} | {r["subtopic"]} | {tags} |')
        A('')

    for lo in sorted(bands):
        A(f'## {lo}&ndash;{lo + BAND - 1}\n')
        table(bands[lo])
    if unrated:
        A('## Unrated\n')
        A('CodeChef publishes no difficulty rating for these.\n')
        table(unrated)

    A('---\n')
    A('Generated by `python3 tools/build_docs.py` - edit '
      '`data/authored/<CODE>.md` or `solutions/<CODE>.py` and rebuild.\n')
    os.makedirs(RATED, exist_ok=True)
    with open(os.path.join(RATED, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L).rstrip() + '\n')


def write_index(built, codes):
    by_topic = defaultdict(list)
    for b in built:
        by_topic[b['topic']].append(b)
    done = {b['code'] for b in built}
    L = []
    A = L.append
    A('# CodeChef - Become 5 Star roadmap\n')
    A('Worked documentation for every problem I have solved on the CodeChef '
      '[Become 5 Star](https://www.codechef.com/roadmap/become-5-star) roadmap: '
      'the question, its constraints, an explained Python solution, the time and '
      'space complexity, and the topic or data structure it belongs to.\n')
    A(f'**{len(built)} of {len(codes)} solved problems documented.**\n')
    A('## Roadmap progress\n')
    A('| Level | Course | Solved | Total | Documented |')
    A('|---|---|---:|---:|---:|')
    for c in IDX['courses']:
        n = sum(1 for b in built if META[b['code']]['course'] == c['slug'])
        A(f'| {c["level"]} | {c["title"]} | {c["solved"]} | {c["total"]} | {n} |')
    A(f'| | **Total** | **{IDX["total_solved"]}** | **{IDX["total_problems"]}** '
      f'| **{len(built)}** |')
    A('')
    note = (f'The roadmap headline counts **{IDX["total_solved"]} solved '
            'entries**, but that sums a per-course counter and a problem can '
            'hold more than one slot. Deduplicated it is '
            f'**{len(codes)} distinct problems**, which is what is documented '
            'here')
    slots = os.path.join(ROOT, 'data', 'roadmap_slots.json')
    if os.path.exists(slots):
        data = json.load(open(slots))
        intra = sum(n - 1 for d in data.values()
                    for n in Counter(d['slots']).values())
        where = defaultdict(set)
        for slug, d in data.items():
            for code in set(d['slots']):
                where[code].add(slug)
        cross = sum(1 for c in codes if len(where.get(c, ())) > 1)
        note += (f': {intra} problems occupy two slots inside a single course '
                 f'and {cross} are listed in two different courses. Run '
                 '`python3 tools/reconcile_counts.py` to reproduce the '
                 'breakdown')
    A(note + '.\n')
    A('## Views\n')
    A('- **[By topic](#problems-by-topic)** - the index below, and '
      '`docs/<topic>/<CODE>.md`.')
    A('- **[By difficulty](by-rating/README.md)** - the same write-ups ordered '
      'by CodeChef rating, in `by-rating/`, each naming the topics used.')
    A('')
    A('## Phases\n')
    A('| Phase | Problems | Documented |')
    A('|---|---:|---:|')
    for i in range(0, len(codes), 100):
        chunk = codes[i:i + 100]
        A(f'| {i // 100 + 1} | {len(chunk)} | {sum(1 for c in chunk if c in done)} |')
    A('')
    A('## Problems by topic\n')
    for topic in sorted(by_topic):
        rows = sorted(by_topic[topic], key=lambda r: r['order'])
        A(f'<details open><summary><b>{topic}</b> ({len(rows)})</summary>\n')
        A('| # | Problem | Difficulty | Technique | Time |')
        A('|---:|---|---:|---|---|')
        for r in rows:
            A(f'| {r["order"]} | [{r["name"]}]({r["path"]}) | {r["rating"]} '
              f'| {r["subtopic"]} | {r["time"]} |')
        A('\n</details>\n')
    A('## Repository layout\n')
    A('```')
    A('docs/<topic>/<CODE>.md       write-ups grouped by topic')
    A('by-rating/<rating>-<CODE>.md the same write-ups in difficulty order')
    A('solutions/<CODE>.py          runnable Python solutions')
    A('data/authored/<CODE>.md      hand written approach + metadata')
    A('data/raw/<CODE>.json         problem payloads fetched from CodeChef')
    A('data/problem_meta.json       code -> contest, course, level, order')
    A('data/roadmap_slots.json      per-course problem slots, for the count audit')
    A('tools/                       fetch, build, verify and audit scripts')
    A('```\n')
    A('## Regenerating\n')
    A('```bash')
    A('python3 tools/fetch_raw.py     # pull problem payloads into data/raw/')
    A('python3 tools/build_docs.py    # rebuild docs/ and this README')
    A('python3 tools/verify.py        # run every solution against its samples')
    A('python3 tools/reconcile_counts.py   # audit the roadmap solved count')
    A('```\n')
    A('Both views are generated, so edit `data/authored/<CODE>.md` or '
      '`solutions/<CODE>.py` and rebuild rather than editing `docs/` or '
      '`by-rating/` directly.\n')
    with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L).rstrip() + '\n')


CPX_ORDER = {}


def main():
    global CPX_ORDER
    codes = open(os.path.join(ROOT, 'data', 'all_solved.txt')).read().split()
    CPX_ORDER = complexity_order(codes)
    built = [build_one(c) for c in codes
             if os.path.exists(os.path.join(AUTH, f'{c}.md'))
             and os.path.exists(os.path.join(SOLN, f'{c}.py'))]
    write_index(built, codes)
    write_rating_index(built)
    cpx = [b for b in built if b['has_extras']]
    write_complexity_index(cpx, CPX_ORDER)
    print(f'built {len(built)} / {len(codes)} docs; '
          f'by-complexity written for {len(cpx)}')


if __name__ == '__main__':
    main()
