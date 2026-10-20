#!/usr/bin/env python3
"""Compact dump of problem payloads for authoring. Usage: dump.py <start> <count>"""
import json, os, sys, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT,'tools'))
import constraints as C
codes = open(os.path.join(ROOT,'data','all_solved.txt')).read().split()
start, count = int(sys.argv[1]), int(sys.argv[2])
def c(s):
    s = (s or '').replace('\r\n','\n').strip()
    return re.sub(r'\n{3,}','\n\n',s)
for i in range(start, min(start+count, len(codes)+1)):
    code = codes[i-1]
    d = json.load(open(os.path.join(ROOT,'data','raw',f'{code}.json')))
    pc = d.get('problemComponents') or {}
    print('='*78)
    print(f'[{i}] {code} :: {d.get("problem_name")} :: rating {d.get("difficulty_rating")} :: tags {d.get("computed_tags")} / {d.get("user_tags")}')
    print('--- STATEMENT'); print(c(pc.get('statement')) or c(d.get('body'))[:1500])
    print('--- INPUT'); print(c(pc.get('inputFormat')))
    print('--- OUTPUT'); print(c(pc.get('outputFormat')))
    print('--- CONSTRAINTS'); print(c(pc.get('constraints')) or OV.get(code,'(none)'))
    s = (pc.get('sampleTestCases') or [{}])[0]
    print('--- SAMPLE IN'); print(c(s.get('input'))[:400])
    print('--- SAMPLE OUT'); print(c(s.get('output'))[:400])
