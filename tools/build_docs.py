#!/usr/bin/env python3
"""
Build docs/<topic>/<CODE>.md from three sources:

  data/raw/<CODE>.json    problem payload fetched from CodeChef
  data/authored/<CODE>.md hand written front matter + "Approach" prose
  solutions/<CODE>.py     the runnable Python solution

Also regenerates README.md with the per-topic index and progress tables.
"""
import html, json, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import constraints as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'data', 'raw')
AUTH = os.path.join(ROOT, 'data', 'authored')
SOLN = os.path.join(ROOT, 'solutions')
DOCS = os.path.join(ROOT, 'docs')

META = json.load(open(os.path.join(ROOT, 'data', 'problem_meta.json')))
IDX = json.load(open(os.path.join(ROOT, 'data', 'roadmap_index.json')))

HTMLISH = re.compile(r'</?(?:p|b|i|u|ul|ol|li|h[1-6]|pre|div|br|strong|em|sub|sup|center|table|tr|td)\b[^>]*>', re.I)


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def parse_authored(path):
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
    return meta, m.group(2).strip()


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


def build_one(code):
    raw = json.load(open(os.path.join(RAW, f'{code}.json'), encoding='utf-8'))
    meta, approach = parse_authored(os.path.join(AUTH, f'{code}.md'))
    solution = open(os.path.join(SOLN, f'{code}.py'), encoding='utf-8').read().rstrip()
    pm = META[code]

    pc = raw.get('problemComponents') or {}
    name = raw.get('problem_name') or code
    rating = raw.get('difficulty_rating') or '?'
    tl = raw.get('max_timelimit') or '?'
    cons = clean(C.resolve(raw, code))
    if not cons:
        print(f'  !! {code}: no constraints', file=sys.stderr)

    # Modern problems keep the prose in `statement`; legacy ones only in `body`.
    statement = clean(pc.get('statement')) or clean(raw.get('body'))

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
    A('## Question\n')
    A(statement + '\n')
    if clean(pc.get('inputFormat')):
        A('**Input**\n')
        A(clean(pc.get('inputFormat')) + '\n')
    if clean(pc.get('outputFormat')):
        A('**Output**\n')
        A(clean(pc.get('outputFormat')) + '\n')
    A('## Constraints\n')
    A((cons or '_Not published for this problem._') + '\n')
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

    A('## Approach\n')
    A(approach + '\n')
    A('## Solution (Python)\n')
    A('```python')
    A(solution)
    A('```\n')
    A('## Complexity\n')
    A(f'- **Time:** {meta["time"]}')
    A(f'- **Space:** {meta["space"]}')
    if meta.get('complexity_note'):
        A(f'- {meta["complexity_note"]}')
    A('')
    tags = [t for t in (raw.get('computed_tags') or []) if t]
    if tags:
        A(f'> CodeChef tags: {", ".join(f"`{t}`" for t in tags)}\n')

    out_dir = os.path.join(DOCS, slugify(topic))
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f'{code}.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(P).rstrip() + '\n')
    return {'code': code, 'name': name, 'rating': rating, 'topic': topic,
            'subtopic': meta.get('subtopic', '-'), 'order': pm['order'],
            'level': pm['level'], 'path': os.path.relpath(out_path, ROOT),
            'time': meta['time']}


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
    A(f'The roadmap counts {IDX["total_solved"]} solved entries across its seven '
      f'courses; {len(codes)} of those are distinct problems (a few appear in two '
      'courses) and that is what is documented here.\n')
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
    A('docs/<topic>/<CODE>.md    generated problem write-ups')
    A('solutions/<CODE>.py       runnable Python solutions')
    A('data/authored/<CODE>.md   hand written approach + metadata')
    A('data/raw/<CODE>.json      problem payloads fetched from CodeChef')
    A('data/problem_meta.json    code -> contest, course, level, order')
    A('tools/                    fetch, build and verify scripts')
    A('```\n')
    A('## Regenerating\n')
    A('```bash')
    A('python3 tools/fetch_raw.py     # pull problem payloads into data/raw/')
    A('python3 tools/build_docs.py    # rebuild docs/ and this README')
    A('python3 tools/verify.py        # run every solution against its samples')
    A('```\n')
    A('Docs are generated, so edit `data/authored/<CODE>.md` or '
      '`solutions/<CODE>.py` and rebuild rather than editing `docs/` directly.\n')
    with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L).rstrip() + '\n')


def main():
    codes = open(os.path.join(ROOT, 'data', 'all_solved.txt')).read().split()
    built = [build_one(c) for c in codes
             if os.path.exists(os.path.join(AUTH, f'{c}.md'))
             and os.path.exists(os.path.join(SOLN, f'{c}.py'))]
    write_index(built, codes)
    print(f'built {len(built)} / {len(codes)} docs')


if __name__ == '__main__':
    main()
