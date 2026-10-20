#!/usr/bin/env python3
"""
Build docs/<topic>/<CODE>.md from three sources:

  data/raw/<CODE>.json   - problem payload pulled from CodeChef (statement,
                           constraints, I/O format, samples, tags, rating)
  data/authored/<CODE>.md- hand written front matter + "Approach" prose
  solutions/<CODE>.py    - the runnable Python solution

Also regenerates README.md with the per-topic index.
"""
import json, os, re, sys, html
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'data', 'raw')
AUTH = os.path.join(ROOT, 'data', 'authored')
SOLN = os.path.join(ROOT, 'solutions')
DOCS = os.path.join(ROOT, 'docs')

COURSE = {'title': '500 to 1000 difficulty rating', 'level': 1,
          'slug': 'logical-problems'}

with open(os.path.join(ROOT, 'data', 'constraints_overrides.json')) as f:
    OVERRIDES = {k: v for k, v in json.load(f).items() if not k.startswith('_')}


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def parse_authored(path):
    """Split `---` front matter from the markdown body."""
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


HTMLISH = re.compile(r'</?(?:p|b|i|u|ul|ol|li|h[1-6]|pre|div|br|strong|em|sub|sup|center)\b[^>]*>', re.I)


def html_to_md(h):
    """Older CodeChef problems store the statement as HTML, not markdown.

    Only recognised tags are stripped, so bare comparison operators such as
    `1 <= N <= 100` survive instead of being eaten as a tag.
    """
    h = re.sub(r'<aside.*?</aside>', '', h, flags=re.S | re.I)
    h = re.sub(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', r'[\2](\1)', h, flags=re.S | re.I)
    h = re.sub(r'<(?:b|strong)\b[^>]*>(.*?)</(?:b|strong)>', r'**\1**', h, flags=re.S | re.I)
    h = re.sub(r'<(?:i|em)\b[^>]*>(.*?)</(?:i|em)>', r'*\1*', h, flags=re.S | re.I)
    h = re.sub(r'<sub\b[^>]*>(.*?)</sub>', r'_\1', h, flags=re.S | re.I)
    h = re.sub(r'<sup\b[^>]*>(.*?)</sup>', r'^\1', h, flags=re.S | re.I)
    h = re.sub(r'<pre\b[^>]*>(.*?)</pre>', lambda m: '\n```\n' + m.group(1).strip() + '\n```\n', h, flags=re.S | re.I)
    h = re.sub(r'<h[1-6]\b[^>]*>(.*?)</h[1-6]>', r'\n\n**\1**\n', h, flags=re.S | re.I)
    h = re.sub(r'<br\s*/?>', '\n', h, flags=re.I)
    h = re.sub(r'<li\b[^>]*>', '- ', h, flags=re.I)
    h = re.sub(r'</(?:p|li|ul|ol|h[1-6]|div)>', '\n', h, flags=re.I)
    h = HTMLISH.sub('', h)
    h = html.unescape(h)
    return h


def clean(md):
    """Normalise a CodeChef field: HTML -> markdown, strip CRs, collapse blanks."""
    if not md:
        return ''
    md = md.replace('\r\n', '\n').replace('\r', '\n')
    if HTMLISH.search(md):
        md = html_to_md(md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    return re.sub(r'\n{3,}', '\n\n', md).strip()


def fence(text):
    """Wrap sample I/O so a stray ``` inside can't break the block."""
    text = (text or '').replace('\r\n', '\n').rstrip()
    bt = '```'
    while bt in text:
        bt += '`'
    return f'{bt}\n{text}\n{bt}'


def build_one(code, idx):
    raw = json.load(open(os.path.join(RAW, f'{code}.json'), encoding='utf-8'))
    meta, approach = parse_authored(os.path.join(AUTH, f'{code}.md'))
    solution = open(os.path.join(SOLN, f'{code}.py'), encoding='utf-8').read().rstrip()

    pc = raw.get('problemComponents') or {}
    name = raw.get('problem_name') or code
    rating = raw.get('difficulty_rating') or '?'
    tl = raw.get('max_timelimit') or '?'
    constraints = clean(pc.get('constraints')) or OVERRIDES.get(code, '')
    if not constraints:
        print(f'  !! {code}: no constraints', file=sys.stderr)

    topic = meta['topic']
    parts = []
    A = parts.append
    A(f'# {idx}. {name}\n')
    A(f'> CodeChef problem code [`{code}`]'
      f'(https://www.codechef.com/problems/{code}) &middot; '
      f'difficulty **{rating}** &middot; time limit **{tl}s**\n')
    A('| | |')
    A('|---|---|')
    A(f'| **Topic** | {topic} |')
    A(f'| **Technique** | {meta.get("subtopic", "-")} |')
    A(f'| **Time** | {meta["time"]} |')
    A(f'| **Space** | {meta["space"]} |')
    A(f'| **Roadmap course** | {COURSE["title"]} (Level {COURSE["level"]}) |')
    A('')

    A('## Question\n')
    A(clean(pc.get('statement')) + '\n')
    if clean(pc.get('inputFormat')):
        A('**Input**\n')
        A(clean(pc.get('inputFormat')) + '\n')
    if clean(pc.get('outputFormat')):
        A('**Output**\n')
        A(clean(pc.get('outputFormat')) + '\n')

    A('## Constraints\n')
    A((constraints or '_Not published for this problem._') + '\n')
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
        f.write('\n'.join(parts).rstrip() + '\n')
    return {'code': code, 'name': name, 'rating': rating, 'topic': topic,
            'subtopic': meta.get('subtopic', '-'), 'idx': idx,
            'path': os.path.relpath(out_path, ROOT),
            'time': meta['time'], 'space': meta['space']}


def main():
    codes = open(os.path.join(ROOT, 'data', 'phase1_codes.txt')).read().split()
    built = []
    for i, code in enumerate(codes, 1):
        if not os.path.exists(os.path.join(AUTH, f'{code}.md')):
            continue
        built.append(build_one(code, i))
    write_index(built, len(codes))
    print(f'built {len(built)} / {len(codes)} docs')


def write_index(built, total):
    by_topic = defaultdict(list)
    for b in built:
        by_topic[b['topic']].append(b)
    L = []
    A = L.append
    A('# CodeChef - Become 5 Star roadmap\n')
    A('Worked documentation for the problems I have solved on the CodeChef '
      '[Become 5 Star](https://www.codechef.com/roadmap/become-5-star) roadmap '
      '- statement, constraints, an explained Python solution, its complexity, '
      'and the topic each problem belongs to.\n')
    A('## Progress\n')
    A('| Level | Course | Solved | Total |')
    A('|---|---|---:|---:|')
    idx = json.load(open(os.path.join(ROOT, 'data', 'roadmap_index.json')))
    for c in idx['courses']:
        A(f'| {c["level"]} | {c["title"]} | {c["solved"]} | {c["total"]} |')
    A(f'| | **Total** | **{idx["total_solved"]}** | **{idx["total_problems"]}** |')
    A('')
    A(f'Documented so far: **{len(built)}** problems.\n')
    A('## Problems by topic\n')
    for topic in sorted(by_topic):
        rows = sorted(by_topic[topic], key=lambda r: r['idx'])
        A(f'### {topic} ({len(rows)})\n')
        A('| # | Problem | Difficulty | Technique | Time |')
        A('|---:|---|---:|---|---|')
        for r in rows:
            A(f'| {r["idx"]} | [{r["name"]}]({r["path"]}) '
              f'| {r["rating"]} | {r["subtopic"]} | {r["time"]} |')
        A('')
    A('## Repository layout\n')
    A('```')
    A('docs/<topic>/<CODE>.md   generated problem write-ups')
    A('solutions/<CODE>.py      runnable Python solutions')
    A('data/raw/<CODE>.json     problem payloads fetched from CodeChef')
    A('data/authored/<CODE>.md  hand written approach + metadata')
    A('tools/                   fetch, build and verify scripts')
    A('```\n')
    A('Docs are generated - edit `data/authored/<CODE>.md` or '
      '`solutions/<CODE>.py` and re-run `python3 tools/build_docs.py`.\n')
    with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L).rstrip() + '\n')


if __name__ == '__main__':
    main()
