#!/usr/bin/env python3
"""
Print a compact digest of problems in by-complexity order, for authoring the
`## Edge cases` and `## Dry run` sections.

    python3 tools/digest.py <start-seq> <count>
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_docs as B
import complexity as X

ROOT = B.ROOT


def main():
    start, count = int(sys.argv[1]), int(sys.argv[2])
    codes = open(os.path.join(ROOT, 'data', 'all_solved.txt')).read().split()
    order = B.complexity_order(codes)
    pick = sorted(((seq, c) for c, (seq, _) in order.items()
                   if start <= seq < start + count))
    for seq, code in pick:
        d = B.load(code)
        key, _ = X.classify(d['meta']['time'])
        print('=' * 78)
        print(f'[{seq:03d}] {code} :: {d["name"]} :: {X.LABEL[key]} :: '
              f'rating {d["rating"]} :: {d["meta"]["topic"]} / '
              f'{d["meta"].get("subtopic")}')
        print(f'--- TIME {d["meta"]["time"]}   SPACE {d["meta"]["space"]}')
        print('--- CONSTRAINTS')
        print((d['cons'] or '(none)')[:600])
        for i, s in enumerate((d['pc'].get('sampleTestCases') or [])[:2], 1):
            print(f'--- SAMPLE {i} IN'); print((s.get('input') or '').strip()[:400])
            print(f'--- SAMPLE {i} OUT'); print((s.get('output') or '').strip()[:400])
        print('--- SOLUTION')
        print(d['solution'])
        print('--- APPROACH')
        print(d['approach'][:900])


if __name__ == '__main__':
    main()
