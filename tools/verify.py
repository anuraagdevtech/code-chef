#!/usr/bin/env python3
"""
Run every solutions/<CODE>.py against the sample tests in data/raw/<CODE>.json
and report whether the output matches.

  PASS     exact match (after whitespace normalisation)
  PASS~    matches ignoring case (fine for YES/NO style answers)
  FAIL     output differs - needs a look
  ERROR    the solution crashed or timed out
  SKIP     no solution file yet

Usage:  python3 tools/verify.py [CODE ...]
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'data', 'raw')
SOLN = os.path.join(ROOT, 'solutions')
TIMEOUT = 15


def norm(s):
    lines = [ln.rstrip() for ln in (s or '').replace('\r\n', '\n').split('\n')]
    while lines and not lines[-1]:
        lines.pop()
    return '\n'.join(lines)


def run(code):
    sol = os.path.join(SOLN, f'{code}.py')
    if not os.path.exists(sol):
        return 'SKIP', ''
    raw = json.load(open(os.path.join(RAW, f'{code}.json'), encoding='utf-8'))
    samples = (raw.get('problemComponents') or {}).get('sampleTestCases') or []
    if not samples:
        return 'SKIP', 'no samples'
    worst, detail = 'PASS', ''
    for i, s in enumerate(samples, 1):
        inp, exp = s.get('input') or '', s.get('output') or ''
        try:
            p = subprocess.run([sys.executable, '-I', sol], input=inp,
                               capture_output=True, text=True, timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            return 'ERROR', f'sample {i}: timeout after {TIMEOUT}s'
        if p.returncode != 0:
            return 'ERROR', f'sample {i}: {p.stderr.strip().splitlines()[-1] if p.stderr.strip() else "exit " + str(p.returncode)}'
        got, want = norm(p.stdout), norm(exp)
        if got == want:
            continue
        if got.lower() == want.lower():
            worst = 'PASS~' if worst == 'PASS' else worst
            continue
        return 'FAIL', f'sample {i}: expected {want!r} got {got!r}'
    return worst, detail


def main():
    codes = sys.argv[1:] or open(os.path.join(ROOT, 'data', 'phase1_codes.txt')).read().split()
    tally = {}
    for code in codes:
        status, detail = run(code)
        tally[status] = tally.get(status, 0) + 1
        if status not in ('PASS', 'SKIP'):
            print(f'{status:6} {code}  {detail}')
        elif status == 'PASS~':
            print(f'{status:6} {code}')
    print('\n' + '  '.join(f'{k}={v}' for k, v in sorted(tally.items())))
    return 1 if tally.get('FAIL') or tally.get('ERROR') else 0


if __name__ == '__main__':
    sys.exit(main())
