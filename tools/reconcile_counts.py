#!/usr/bin/env python3
"""
Explain the gap between the roadmap's headline "solved" number and the number
of distinct problems documented here.

The roadmap page sums a per-course counter, and a problem can occupy more than
one slot: twice inside the same course, or once in each of two courses. This
script pulls each course's public syllabus (the problem lists are not behind
the login; only the per-user status is) and reports the duplication.

    python3 tools/reconcile_counts.py            # use data/roadmap_slots.json
    python3 tools/reconcile_counts.py --refetch  # re-pull the syllabi first
"""
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLOTS = os.path.join(ROOT, 'data', 'roadmap_slots.json')
IDX = json.load(open(os.path.join(ROOT, 'data', 'roadmap_index.json')))
API = 'https://www.codechef.com/api/practice/syllabus/'


def fetch(slug):
    """Shell out to curl: this interpreter has no CA bundle for urllib."""
    out = subprocess.run(
        ['curl', '-s', '--max-time', '30', '-H', 'User-Agent: Mozilla/5.0',
         API + slug], capture_output=True)
    d = json.loads(out.stdout)
    slots = []
    for mod in d.get('modules') or []:
        for sm in mod.get('submodules') or []:
            for p in sm.get('problems_with_status') or []:
                slots.append(p['code'])
    return {'total_problems': d.get('total_problems'), 'slots': slots}


def refetch():
    data = {c['slug']: fetch(c['slug']) for c in IDX['courses']}
    json.dump(data, open(SLOTS, 'w'), indent=1, sort_keys=True)
    return data


def main():
    if '--refetch' in sys.argv or not os.path.exists(SLOTS):
        data = refetch()
        print(f'wrote {SLOTS}')
    else:
        data = json.load(open(SLOTS))

    solved = set(open(os.path.join(ROOT, 'data', 'all_solved.txt')).read().split())
    reported = {c['slug']: c['solved'] for c in IDX['courses']}
    where = defaultdict(set)
    intra = 0

    print(f'{"course":<30}{"slots":>7}{"distinct":>9}{"reported":>9}{"mine":>6}')
    for slug, d in sorted(data.items(), key=lambda kv: -len(kv[1]['slots'])):
        counts = Counter(d['slots'])
        intra += sum(n - 1 for n in counts.values())
        mine = len(set(counts) & solved)
        for code in counts:
            where[code].add(slug)
        print(f'{slug:<30}{len(d["slots"]):>7}{len(counts):>9}'
              f'{reported.get(slug, 0):>9}{mine:>6}')

    cross = [c for c, s in where.items() if c in solved and len(s) > 1]
    print()
    print(f'roadmap headline solved entries        : {IDX["total_solved"]}')
    print(f'distinct problems marked solved        : {len(solved)}')
    print(f'problems holding two slots in one course: {intra}')
    print(f'problems listed in two courses          : {len(cross)}')
    print()
    print('slots repeated inside one course:')
    for slug, d in sorted(data.items()):
        for code, n in sorted(Counter(d['slots']).items()):
            if n > 1:
                print(f'  {code:<14} x{n} in {slug}')
    print('\nlisted in more than one course:')
    for code in sorted(cross):
        print(f'  {code:<14} {", ".join(sorted(where[code]))}')


if __name__ == '__main__':
    main()
