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
    # Statements carry their own "### Input" style headings; demote them so the
    # write-up keeps a single heading hierarchy of its own.
    md = re.sub(r'^#{1,6} *(.+?)\s*$', r'**\1**', md, flags=re.M)
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


def extras_body(d, A):
    """Edge cases and dry run - shared by both views."""
    sec = d['sections']
    if 'edge cases' in sec:
        A('## Edge cases\n')
        A(sec['edge cases'] + '\n')
    if 'dry run' in sec:
        A('## Dry run\n')
        A(sec['dry run'] + '\n')


def rating_order(codes):
    """Sequence number per code: easiest rating first, unrated last."""
    rows = []
    for c in codes:
        raw = json.load(open(os.path.join(RAW, f'{c}.json'), encoding='utf-8'))
        r = raw.get('difficulty_rating')
        r = int(r) if str(r).lstrip('-').isdigit() else -1
        # Unrated problems have no place on the ladder, so they go at the end.
        rows.append((r if r > 0 else 10 ** 7, c))
    rows.sort()
    return {c: i + 1 for i, (_, c) in enumerate(rows)}


def render_study(d, seq):
    """by-rating view: one file per problem, in rating order, with the
    topic, constraints, approach, solution, edge cases and a dry run."""
    meta, pm, sec = d['meta'], d['pm'], d['sections']
    cls, cls_note = X.classify(meta['time'])
    rating = d['rating'] if d['rating'] > 0 else 'unrated'
    ready = {'edge cases', 'dry run'} <= set(sec)
    P = []
    A = P.append
    prev, nxt = NAV_RATED.get(d['code'], (None, None))
    A(nav_line(prev, nxt, 'README.md') + '\n')
    A(f'# {seq:03d}. {d["name"]}\n')
    A(f'> [`{d["code"]}`](https://www.codechef.com/problems/{d["code"]}) '
      f'&middot; difficulty **{rating}** '
      f'&middot; time limit **{d["timelimit"]}s** '
      f'&middot; {pm["course_title"]} (Level {pm["level"]})\n')
    if not ready:
        A('> _Edge cases and dry run for this problem are still to be '
          'written._\n')

    A('## Topic used\n')
    A('| | |')
    A('|---|---|')
    A(f'| **Topic** | {meta["topic"]} |')
    A(f'| **Technique** | {meta.get("subtopic", "-")} |')
    if d['tags']:
        A(f'| **CodeChef tags** | {", ".join(f"`{t}`" for t in d["tags"])} |')
    A(f'| **Complexity class** | {X.LABEL[cls]} {X.CANON[cls]}'
      f'{" (" + cls_note + ")" if cls_note else ""} |')
    A(f'| **Time** | {meta["time"]} |')
    A(f'| **Space** | {meta["space"]} |')
    A('')

    problem_body(d, A)

    A('## Approach\n')
    A(d['approach'] + '\n')

    A('## Solution\n')
    A('```python')
    A(d['solution'])
    A('```\n')

    extras_body(d, A)

    rel = os.path.join('..', 'docs', slugify(meta['topic']), f'{d["code"]}.md')
    A('---\n')
    A(f'Same problem grouped by topic: [{rel}]({rel})\n')
    return '\n'.join(P).rstrip() + '\n'


BAND = 200


def write_study_index(built, order):
    """by-rating/README.md: the whole ladder, grouped into rating bands."""
    by_code = {b['code']: b for b in built}
    rows = sorted(((seq, c) for c, seq in order.items()))
    done = sum(1 for _, c in rows if by_code[c]['has_extras'])
    bands = defaultdict(list)
    for seq, c in rows:
        r = by_code[c]['num_rating']
        bands['unrated' if r <= 0 else r // BAND * BAND].append((seq, c))
    keys = sorted(k for k in bands if k != 'unrated')

    L = []
    A = L.append
    f_seq, f_code = rows[0]
    A(f'[&larr; Repository index](../README.md) &middot; '
      f'[{f_seq:03d}. {by_code[f_code]["name"]} &rarr;]'
      f'({f_seq:03d}-{f_code}.md)\n')
    A('# Problems in rating order\n')
    A('Every solved problem, ordered by CodeChef difficulty rating and '
      'numbered so a plain directory listing follows the same order: '
      '`001-<CODE>.md` is the easiest, `486-<CODE>.md` the hardest. One file '
      'per problem, each carrying the topic used, the problem and its '
      'constraints, the approach, the solution, its edge cases and a dry '
      'run.\n')
    written = ('**every one** carrying edge cases and a dry run'
               if done == len(rows)
               else f'**{done} of them** carrying edge cases and a dry run')
    A(f'**{len(rows)} problems** &middot; ratings '
      f'{by_code[rows[0][1]]["num_rating"]} upward &middot; {written}. Problems '
      'CodeChef has not rated carry no place on the ladder, so they sit at '
      'the end.\n')
    A('Same write-ups grouped by topic instead: [`../docs`](../docs).\n')

    A('## Bands\n')
    A('| Band | Problems | Written | Most common topic |')
    A('|---|---:|---:|---|')
    for k in keys:
        rs = bands[k]
        top = Counter(by_code[c]['topic'] for _, c in rs).most_common(1)[0]
        A(f'| [{k}&ndash;{k + BAND - 1}](#{k}{k + BAND - 1}) | {len(rs)} '
          f'| {sum(1 for _, c in rs if by_code[c]["has_extras"])} '
          f'| {top[0]} ({top[1]}) |')
    if 'unrated' in bands:
        rs = bands['unrated']
        top = Counter(by_code[c]['topic'] for _, c in rs).most_common(1)[0]
        A(f'| [Unrated](#unrated) | {len(rs)} '
          f'| {sum(1 for _, c in rs if by_code[c]["has_extras"])} '
          f'| {top[0]} ({top[1]}) |')
    A('')

    def table(rs):
        A('| # | Problem | Rating | Topic | Technique | Edge cases + dry run |')
        A('|---:|---|---:|---|---|:---:|')
        for seq, c in rs:
            b = by_code[c]
            shown = b['num_rating'] if b['num_rating'] > 0 else '&ndash;'
            mark = 'yes' if b['has_extras'] else '&ndash;'
            A(f'| {seq:03d} | [{b["name"]}]({seq:03d}-{c}.md) `{c}` '
              f'| {shown} | {b["topic"]} | {b["subtopic"]} | {mark} |')
        A('')

    for k in keys:
        A(f'## {k}&ndash;{k + BAND - 1}\n')
        table(bands[k])
    if 'unrated' in bands:
        A('## Unrated\n')
        A('CodeChef publishes no difficulty rating for these.\n')
        table(bands['unrated'])

    A('---\n')
    A('Generated by `python3 tools/build_docs.py` - edit '
      '`data/authored/<CODE>.md` or `solutions/<CODE>.py` and rebuild.\n')
    os.makedirs(RATED, exist_ok=True)
    with open(os.path.join(RATED, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L).rstrip() + '\n')


NAV_RATED = {}
NAV_TOPIC = {}


def nav_line(prev, nxt, index_href):
    """A 'back | index | next' row. prev/nxt are (label, href) or None."""
    parts = []
    if prev:
        parts.append(f'[&larr; {prev[0]}]({prev[1]})')
    parts.append(f'[Index]({index_href})')
    if nxt:
        parts.append(f'[{nxt[0]} &rarr;]({nxt[1]})')
    return ' &middot; '.join(parts)


def build_nav(codes):
    """Neighbour links for both views: rating order, and order within topic."""
    name, topic = {}, {}
    for c in codes:
        raw = json.load(open(os.path.join(RAW, f'{c}.json'), encoding='utf-8'))
        name[c] = raw.get('problem_name') or c
        topic[c] = parse_authored(os.path.join(AUTH, f'{c}.md'))[0]['topic']

    ladder = sorted(codes, key=lambda c: SEQ[c])

    def rated_ref(j):
        if not 0 <= j < len(ladder):
            return None
        o = ladder[j]
        return (f'{SEQ[o]:03d}. {name[o]}', f'{SEQ[o]:03d}-{o}.md')

    for i, c in enumerate(ladder):
        NAV_RATED[c] = (rated_ref(i - 1), rated_ref(i + 1))

    groups = defaultdict(list)
    for c in codes:
        groups[topic[c]].append(c)
    for members in groups.values():
        members.sort(key=lambda c: META[c]['order'])

        def topic_ref(j, members=members):
            if not 0 <= j < len(members):
                return None
            o = members[j]
            return (f'{META[o]["order"]}. {name[o]}', f'{o}.md')

        for i, c in enumerate(members):
            NAV_TOPIC[c] = (topic_ref(i - 1), topic_ref(i + 1))


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
    prev, nxt = NAV_TOPIC.get(code, (None, None))
    A(nav_line(prev, nxt, os.path.join('..', '..', 'README.md')) + '\n')
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
    extras_body(d, A)
    tags = [t for t in (raw.get('computed_tags') or []) if t]
    if tags:
        A(f'> CodeChef tags: {", ".join(f"`{t}`" for t in tags)}\n')
    seq = SEQ[code]
    rated_rel = os.path.join('..', '..', 'by-rating', f'{seq:03d}-{code}.md')
    A('---\n')
    A(f'Same problem in rating order (#{seq} of {len(SEQ)}): '
      f'[{rated_rel}]({rated_rel})\n')

    out_dir = os.path.join(DOCS, slugify(topic))
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f'{code}.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(P).rstrip() + '\n')

    os.makedirs(RATED, exist_ok=True)
    with open(os.path.join(RATED, f'{seq:03d}-{code}.md'),
              'w', encoding='utf-8') as f:
        f.write(render_study(d, seq))

    return {'code': code, 'name': name, 'rating': rating, 'topic': topic,
            'subtopic': meta.get('subtopic', '-'), 'order': pm['order'],
            'level': pm['level'], 'path': os.path.relpath(out_path, ROOT),
            'time': meta['time'], 'num_rating': d['rating'],
            'tags': d['tags'],
            'best_tag': d['best_tag'],
            'has_extras': {'edge cases', 'dry run'} <= set(d['sections'])}


def write_index(built, codes):
    by_topic = defaultdict(list)
    for b in built:
        by_topic[b['topic']].append(b)
    done = {b['code'] for b in built}
    L = []
    A = L.append
    ladder = sorted(done, key=lambda c: SEQ[c])
    if ladder:
        first = ladder[0]
        name = next(b['name'] for b in built if b['code'] == first)
        A(f'[Rating-ordered index](by-rating/README.md) &middot; '
          f'[{SEQ[first]:03d}. {name} &rarr;]'
          f'(by-rating/{SEQ[first]:03d}-{first}.md)\n')
    A('# CodeChef - Become 5 Star roadmap\n')
    A('Worked documentation for every problem I have solved on the CodeChef '
      '[Become 5 Star](https://www.codechef.com/roadmap/become-5-star) roadmap: '
      'the question, its constraints, an explained Python solution, the time '
      'and space complexity, the topic or data structure it belongs to, the '
      'edge cases that decide the problem, and a dry run on a sample.\n')
    A(f'**{len(built)} of {len(codes)} solved problems documented.**\n')
    A('## Roadmap progress\n')
    A('| Level | Course | Solved | Total | Files here |')
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
                 f'and {cross} are listed in two different courses. A '
                 'problem listed in two courses is written up once and filed '
                 'under one of them, which is why the per-course **Files '
                 'here** column can sit below that course\'s **Solved** '
                 'count while the totals still agree. Run '
                 '`python3 tools/reconcile_counts.py` to reproduce the '
                 'breakdown')
    A(note + '.\n')
    A('## Views\n')
    A('Every problem is written up once and rendered into two views, which '
      'carry the same six sections and cross-link to each other.\n')
    A('- **[By topic](#problems-by-topic)** - the index below, and '
      '`docs/<topic>/<CODE>.md`.')
    A(f'- **[By rating](by-rating/README.md)** - the same {len(built)} '
      'problems numbered `001`-`'
      f'{len(built):03d}` in difficulty order, so a plain directory listing '
      'runs easiest to hardest.')
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
    A('by-rating/<NNN>-<CODE>.md   the same problems in rating order')
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


SEQ = {}


def main():
    global SEQ
    codes = open(os.path.join(ROOT, 'data', 'all_solved.txt')).read().split()
    SEQ = rating_order(codes)
    have = [c for c in codes
            if os.path.exists(os.path.join(AUTH, f'{c}.md'))
            and os.path.exists(os.path.join(SOLN, f'{c}.py'))]
    build_nav(have)
    built = [build_one(c) for c in codes
             if os.path.exists(os.path.join(AUTH, f'{c}.md'))
             and os.path.exists(os.path.join(SOLN, f'{c}.py'))]
    write_index(built, codes)
    write_study_index(built, SEQ)
    extras = sum(1 for b in built if b['has_extras'])
    print(f'built {len(built)} / {len(codes)} docs in two views; '
          f'{extras} have edge cases and a dry run')


if __name__ == '__main__':
    main()
