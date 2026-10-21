#!/usr/bin/env python3
r"""
Classify every problem's solution by time complexity, so they can be ordered
from the cheapest algorithm to the dearest.

The class is the cost of **one test case**, expressed in the bounds the problem
itself states, because that is what dominates as T grows. Two conventions
follow from that:

  * a cost written "per query" or "per item" is multiplied up, so
    "O(1) per query" is linear in Q for the test case;
  * work proportional to the digit count of a value is logarithmic in that
    value, matching how the rest of these write-ups use O(log N);
  * a one-off sieve or table build is not part of the class, but is flagged.

There are only 121 distinct `time:` strings across the 486 problems, so each is
assigned a class by hand in TABLE below rather than parsed heuristically - a
mis-parse would silently mis-sort, and the table is auditable. `python3
tools/complexity.py` prints the grouping for review, and the build fails loudly
if a new `time:` string appears that the table does not cover.
"""
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# rank, key, canonical form, label
CLASSES = [
    (1, 'constant', r'$O(1)$', 'Constant time'),
    (2, 'log', r'$O(\log n)$', 'Logarithmic'),
    (3, 'polylog', r'$O(\log^2 n)$', 'Polylogarithmic'),
    (4, 'sqrt', r'$O(\sqrt{n})$', 'Square root'),
    (5, 'linear', r'$O(n)$', 'Linear'),
    (6, 'near-linear', r'$O(n \log \log n)$', 'Near-linear'),
    (7, 'linearithmic', r'$O(n \log n)$', 'Linearithmic'),
    (8, 'n-polylog', r'$O(n \log^2 n)$', 'Linear times polylog'),
    (9, 'product', r'$O(n m)$', 'Product of two sizes'),
    (10, 'quadratic', r'$O(n^2)$', 'Quadratic'),
]
RANK = {k: r for r, k, _, _ in CLASSES}
CANON = {k: c for _, k, c, _ in CLASSES}
LABEL = {k: l for _, k, _, l in CLASSES}

TABLE = {
    # --- constant -----------------------------------------------------------
    r'$O(1)$ per test case': 'constant',
    r'$O(1)$': 'constant',
    r'$O(1)$ — a fixed-width scan': 'constant',
    r'$O(1)$ — at most 10 divisibility tests': 'constant',
    r'$O(1)$ per test case — eight combinations': 'constant',
    r'$O(1)$ per test case — ten fixed difficulties': 'constant',
    r'$O(1)$ per test case — ten fixed entries': 'constant',
    r'$O(1)$ per test case — twelve candidate assignments': 'constant',
    r'$O(1)$ per test case — the search is bounded by a small constant': 'constant',
    r'$O(1)$ per test case in practice': 'constant',
    r'$O(1)$ per test case (12 fixed matches)': 'constant',
    r'$O(1)$ per test case after an $O(N)$ precomputation': 'constant',
    r'$O(\sqrt[2]{N})$-free, $O(1)$ per test case': 'constant',
    r'$O(V \log \log V + 5V)$ precomputation, $O(1)$ per query': 'constant',
    r'$O(20)$ per test case': 'constant',
    r'$O(k)$ per test case, $k = 6$ denominations': 'constant',
    r'$O(L)$ per test case with $L = 5$': 'constant',
    r'$O(2^k)$ per test case with $k = 3$, so $O(1)$': 'constant',
    r'$O(d \log d)$ per test case with $d \leq 7$ digits': 'constant',
    r'$O(N/100)$ per test case — at most 11 iterations': 'constant',
    # --- logarithmic --------------------------------------------------------
    r'$O(\log N)$ per test case': 'log',
    r'$O(\log M)$ per test case': 'log',
    r'$O(\log K)$ per test case': 'log',
    r'$O(\log R)$ per test case': 'log',
    r'$O(\log S)$ per test case': 'log',
    r'$O(\log N + \log M)$ per test case': 'log',
    r'$O(\log \min(X,Y))$ per test case': 'log',
    r'$O(\log \min(A,B))$ per test case': 'log',
    r'$O(\log \min(B,D))$ per test case': 'log',
    r'$O(\log \min(N,M))$ per test case': 'log',
    r'$O(\log \min(N,K))$ per test case': 'log',
    r'$O(\log C)$ per test case after an $O(C \log C)$ precomputation': 'log',
    r'$O(\log H)$ per test case after an $O(V \log\log V)$ sieve': 'log',
    r'$O(d)$': 'log',
    r'$O(d)$ per test case': 'log',
    r'$O(d)$ per test case, $d$ = number of digits': 'log',
    # --- polylogarithmic ----------------------------------------------------
    r'$O(\log^2 N)$ per test case': 'polylog',
    r'$O(\log^2 \max(A,B))$ per test case': 'polylog',
    r'$O(\log A \cdot \log B)$ per test case': 'polylog',
    r'$O(g \log^3 X)$ per test case, where $g$ is the local prime gap': 'polylog',
    # --- square root --------------------------------------------------------
    r'$O(\sqrt{N})$ per test case': 'sqrt',
    r'$O(\sqrt{S})$ per test case': 'sqrt',
    r'$O(\sqrt{Y})$ per test case': 'sqrt',
    r'$O(\sqrt{c})$ per test case': 'sqrt',
    r'$O(\sqrt{|A-B|})$ per test case': 'sqrt',
    # --- linear -------------------------------------------------------------
    r'$O(N)$ per test case': 'linear',
    r'$O(N)$': 'linear',
    r'$O(n)$ per test case': 'linear',
    r'$O(n)$': 'linear',
    r'$O(n)$ overall': 'linear',
    r'$O(N)$ per test case, all of it input reading': 'linear',
    r'$O(|S|)$ per test case': 'linear',
    r'$O(|S|)$': 'linear',
    r'$O(|s|)$ per test case': 'linear',
    r'$O(|A|)$ per test case': 'linear',
    r'$O(|H|)$ per test case': 'linear',
    r'$O(|X|)$ per test case': 'linear',
    r'$O(|W|)$ per word': 'linear',
    r'$O(K)$ per test case': 'linear',
    r'$O(D)$ per test case': 'linear',
    r'$O(S)$ per test case': 'linear',
    r'$O(P)$ per test case': 'linear',
    r'$O(L)$ per report': 'linear',
    r'$O(N + M)$ per test case': 'linear',
    r'$O(N + Q)$ per test case': 'linear',
    r'$O(N + K)$ per test case': 'linear',
    r'$O(N + V)$ per test case': 'linear',
    r'$O(N + V)$ per test case with $V = 100$': 'linear',
    r'$O(N + \max L)$ per test case': 'linear',
    r'$O(M + K)$ per test case': 'linear',
    r'$O(X + Y)$ per test case': 'linear',
    r'$O(100 + M)$ per test case': 'linear',
    r'$O(31(N + Q))$': 'linear',
    r'$O(\sum E_i)$ per test case': 'linear',
    r'$O(\sum |S_i|)$ per test case': 'linear',
    r'$O(n + \log 360)$ per test case': 'linear',
    r'$O(n)$ big-integer multiplications per test case': 'linear',
    "$O(|S| + 26 h)$ per test case, where $h$ is the number of '#'": 'linear',
    r'$O(\sqrt{R} \log\log \sqrt{R} + (R-L))$ per test case': 'linear',
    r'$O(V \log\log V)$ once, then $O(m - n)$ per query': 'linear',
    r'$O(1)$ amortised per action, $O(N)$ overall': 'linear',
    r'$O(1)$ per query': 'linear',
    r'$O(1)$ per contestant': 'linear',
    r'$O(d)$ per number': 'linear',
    # --- near-linear --------------------------------------------------------
    r'$O(N \log \log N)$ per test case': 'near-linear',
    r'$O((N + M)\,\alpha(N))$ per test case': 'near-linear',
    # --- linearithmic -------------------------------------------------------
    r'$O(N \log N)$ per test case': 'linearithmic',
    r'$O(N \log N)$': 'linearithmic',
    r'$O(M \log M)$': 'linearithmic',
    r'$O(M \log M)$ per test case': 'linearithmic',
    r'$O(N \log A)$ per test case': 'linearithmic',
    r'$O(N \log \max A)$ per test case': 'linearithmic',
    r'$O(N \log A + Q \log A)$ per test case': 'linearithmic',
    r'$O(N \log V + \log^2 V)$ per test case': 'linearithmic',
    r'$O(N \log N + P)$': 'linearithmic',
    r'$O(N \log N + Q)$': 'linearithmic',
    r'$O(N \log N + 30 \log N)$ per test case': 'linearithmic',
    r'$O(N \log N + L)$, where $L$ is the number of moves reached': 'linearithmic',
    r'$O(N \log \frac{1}{\varepsilon})$ per test case': 'linearithmic',
    r'$O(N \log(\text{months}))$': 'linearithmic',
    r'$O((N + M) \log N)$ per test case': 'linearithmic',
    r'$O((N + D) \log N)$ per test case': 'linearithmic',
    r'$O((N + Q) \log N)$ per test case': 'linearithmic',
    r'$O(K \log K + n \log n)$ per test case, where $n = \max q_i$': 'linearithmic',
    # --- linear times polylog ----------------------------------------------
    r'$O(m \log m \log(\text{time}))$ per test case': 'n-polylog',
    # --- product of two sizes ----------------------------------------------
    r'$O(NM)$ per test case': 'product',
    r'$O(nm)$ per test case': 'product',
    r'$O(N \cdot M)$ per test case': 'product',
    r'$O(NK)$ per test case': 'product',
    r'$O(N \cdot K)$': 'product',
    r'$O(R \cdot C)$ per test case': 'product',
    r'$O(H \cdot M)$ per test case': 'product',
    r'$O(N \cdot d)$ per test case after an $O(M)$ sieve': 'product',
    r'$O(nm + n \log m)$ per test case': 'product',
    # --- quadratic ----------------------------------------------------------
    r'$O(N^2)$ per test case': 'quadratic',
    r'$O(n^2)$': 'quadratic',
    r'$O(K^2)$ per test case': 'quadratic',
    r'$O(N^2)$ per test case at these bounds, or $O(N \log N)$ sorted': 'quadratic',
    r'$O(n + \text{inversions})$': 'quadratic',
    r'$O(m \min(K, m))$ after an $O(N)$ tally, where $m$ is the number of distinct values': 'quadratic',
    r'$O(|S|)$ per test case for the cost scan, plus $O(|S|)$ per tied placement': 'quadratic',
}

PRECOMP_WORDS = ('sieve', 'precomputation', 'once,', 'tally')


def classify(time_text):
    """(class key, note). Raises if the string is not in the table."""
    key = TABLE.get(time_text)
    if key is None:
        raise KeyError(f'unclassified time string: {time_text!r}\n'
                       f'add it to TABLE in tools/complexity.py')
    low = time_text.lower()
    note = 'one-off precomputation' if any(w in low for w in PRECOMP_WORDS) else ''
    return key, note


def time_of(code):
    path = os.path.join(ROOT, 'data', 'authored', f'{code}.md')
    for line in open(path, encoding='utf-8').read().split('---')[1].splitlines():
        if line.startswith('time:'):
            return line[5:].strip()
    raise ValueError(f'{code}: no time: line')


if __name__ == '__main__':
    import collections
    buckets = collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(ROOT, 'data', 'authored', '*.md'))):
        code = os.path.basename(p)[:-3]
        t = time_of(code)
        buckets[classify(t)[0]].append((t, code))
    total = 0
    for rank, key, canon, label in CLASSES:
        rows = buckets.get(key, [])
        total += len(rows)
        print(f'\n=== {rank}. {label}  {canon}  ({len(rows)} problems) ===')
        seen = collections.defaultdict(list)
        for t, code in rows:
            seen[t].append(code)
        for t in sorted(seen, key=lambda x: (-len(seen[x]), x)):
            extra = '' if len(seen[t]) > 3 else '  ' + ' '.join(sorted(seen[t]))
            print(f'  {len(seen[t]):>3}  {t}{extra}')
    print(f'\ntotal classified: {total}')
