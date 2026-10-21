#!/usr/bin/env python3
"""
Add or replace the `## Edge cases` and `## Dry run` sections of
data/authored/<CODE>.md, reading a JSON map from stdin:

    {"CODE": {"edge cases": "...", "dry run": "..."}, ...}

Idempotent: re-running with the same input leaves the files unchanged.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ['edge cases', 'dry run']
TITLE = {'edge cases': 'Edge cases', 'dry run': 'Dry run'}


def main():
    payload = json.load(sys.stdin)
    for code, sections in payload.items():
        path = os.path.join(ROOT, 'data', 'authored', f'{code}.md')
        text = open(path, encoding='utf-8').read()
        m = re.match(r'^(---\n.*?\n---\n?)(.*)$', text, flags=re.S)
        front, body = m.group(1), m.group(2)
        parts = re.split(r'^## +(.+?)\s*$', body, flags=re.M)
        have = {parts[i].strip().lower(): parts[i + 1].strip()
                for i in range(1, len(parts) - 1, 2)}
        have.update({k.lower(): v.strip() for k, v in sections.items()})
        out = [parts[0].strip()]
        for key in ORDER:
            if key in have:
                out.append(f'## {TITLE[key]}\n\n{have[key]}')
        for key in have:
            if key not in ORDER:
                out.append(f'## {key.title()}\n\n{have[key]}')
        open(path, 'w', encoding='utf-8').write(front + '\n\n'.join(out) + '\n')
    print(f'updated {len(payload)} authored files')


if __name__ == '__main__':
    main()
