#!/usr/bin/env python3
"""
Fetch CodeChef problem payloads into data/raw/<CODE>.json.

The practice problem endpoint needs no authentication:
    GET /api/contests/{contest}/problems/{code}

Most roadmap problems answer to the pseudo-contest PRACTICE, but ~28% of them
only resolve under the contest code their course lists (LP1TO201, DIFF1500,
...), so the contest comes from data/problem_meta.json.

Usage:  python3 tools/fetch_raw.py [CODE ...]      (default: all solved)
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'data', 'raw')
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36')
META = json.load(open(os.path.join(ROOT, 'data', 'problem_meta.json')))
REMAINING_META = os.path.join(ROOT, 'data', 'remaining_problem_meta.json')
if os.path.exists(REMAINING_META):
    META.update(json.load(open(REMAINING_META)))


def get(url):
    """Shell out to curl: this interpreter has no configured CA bundle, so
    urllib raises CERTIFICATE_VERIFY_FAILED against codechef.com."""
    p = subprocess.run(
        ['curl', '-sS', '-m', '30', '-H', f'User-Agent: {UA}',
         '-H', 'Accept: application/json', url],
        capture_output=True, text=True, timeout=40)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip()[:200])
    return json.loads(p.stdout)


def ok(d):
    if not d or d.get('status') == 'error':
        return False
    pc = d.get('problemComponents') or {}
    return bool((pc.get('statement') or '').strip() or (d.get('body') or '').strip())


def fetch_one(code):
    out = os.path.join(RAW, f'{code}.json')
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return code, 'cached'
    # Try the problem's own contest first, then the generic PRACTICE pool.
    contests = [META.get(code, {}).get('contest'), 'PRACTICE']
    for c in [x for x in contests if x]:
        try:
            d = get(f'https://www.codechef.com/api/contests/{c}/problems/{code}')
        except Exception as e:
            continue
        if ok(d):
            with open(out, 'w', encoding='utf-8') as f:
                json.dump(d, f)
            return code, f'ok({c})'
    return code, 'FAILED'


def main():
    if sys.argv[1:] == ['--remaining']:
        codes = open(os.path.join(ROOT, 'data', 'remaining.txt')).read().split()
    else:
        codes = sys.argv[1:] or open(os.path.join(ROOT, 'data', 'all_solved.txt')).read().split()
    os.makedirs(RAW, exist_ok=True)
    failed = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for code, status in ex.map(fetch_one, codes):
            if status == 'FAILED':
                failed.append(code)
    print(f'fetched {len(codes) - len(failed)} / {len(codes)}')
    if failed:
        print('FAILED:', ' '.join(failed))


if __name__ == '__main__':
    main()

