#!/usr/bin/env python3
"""Compact dump of problem payloads for authoring.

Usage: python3 tools/dump.py <start-index> <count>   (1-based, roadmap order)
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import constraints as C
from build_docs import clean

codes = open(os.path.join(ROOT, 'data', 'all_solved.txt')).read().split()
start, count = int(sys.argv[1]), int(sys.argv[2])

for i in range(start, min(start + count, len(codes) + 1)):
    code = codes[i - 1]
    d = json.load(open(os.path.join(ROOT, 'data', 'raw', f'{code}.json')))
    pc = d.get('problemComponents') or {}
    print('=' * 78)
    print(f'[{i}] {code} :: {d.get("problem_name")} :: rating {d.get("difficulty_rating")} '
          f':: tags {d.get("computed_tags")} / {d.get("user_tags")}')
    stmt = clean(pc.get('statement')) or clean(d.get('body'))
    print('--- STATEMENT'); print(stmt[:1800])
    if clean(pc.get('inputFormat')):
        print('--- INPUT'); print(clean(pc.get('inputFormat')))
    if clean(pc.get('outputFormat')):
        print('--- OUTPUT'); print(clean(pc.get('outputFormat')))
    print('--- CONSTRAINTS'); print(clean(C.resolve(d, code)) or '(none)')
    s = (pc.get('sampleTestCases') or [{}])[0]
    print('--- SAMPLE IN'); print((s.get('input') or '')[:350])
    print('--- SAMPLE OUT'); print((s.get('output') or '')[:350])
