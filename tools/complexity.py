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

Each distinct `time:` string is assigned a class by hand in TABLE below
rather than parsed heuristically - a
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
    (11, 'graph-output', r'$O(E \log E + V^2)$', 'Edge sorting and quadratic output'),
    (12, 'matrix-dp', r'$O(M^3 + NM^2)$', 'Cubic transfer and stage DP'),
    (13, 'subset-dp', r'$O(2^K K^2)$', 'Exponential subset DP'),
    (14, 'trial-factor', r'$O(N \pi(\sqrt V))$', 'Trial factorisation'),
    (15, 'bit-knapsack', r'$O(ND/w)$', 'Bitset knapsack'),
    (16, 'budget-dp', r'$O((N+M) \log M + KB)$', 'Interval sweep and budget DP'),
    (17, 'n-sqrt', r'$O(n \sqrt{n})$', 'Linear times square root'),
    (18, 'high-poly', r'$O(n^3)$ and above', 'Cubic or higher polynomial'),
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

# Explicit classes for the additional roadmap algorithms.
TABLE.update({
    '$O(N \\log V)$ per test case': 'linearithmic',
    '$O(N)$ expected per test case': 'linear',
    '$O(N+\\log K)$ per test case': 'linear',
    '$O(P\\log P+Q\\log Q+R\\log R)$ per test case': 'linearithmic',
    '$O(\\log V)$ per test case': 'log',
    '$O(N\\log N)$ per test case': 'linearithmic',
    '$O(NB+Q)$ per test case for $B$ queried bits': 'product',
    '$O(N\\log V)$ per test case': 'linearithmic',
    '$O(|S|+26^2)$ per test case': 'linear',
    '$O(\\log N)$ per test case after $O(\\log N_{max})$ fixed-size matrix preprocessing': 'log',
    '$O(\\sum |A_i|+\\sum |B_i|)$ per test case': 'linear',
    '$O(\\sum |S_i|+26N)$ overall': 'linear',
    '$O(N)$ overall': 'linear',
    '$O((N+Q)\\alpha(N))$ overall': 'near-linear',
    '$O(N+M)$ per test case': 'linear',
    '$O(N)$ expected overall': 'linear',
    '$O(N+E)$ overall': 'linear',
    '$O(N+M\\log M)$ per test case': 'linearithmic',
    '$O(N+M)$ overall': 'linear',
    '$O((N+M)\\log N)$ per test case': 'linearithmic',
    '$O(N^2\\log V)$ per test case with $V=50$': 'quadratic',
    '$O((N+R)\\log N)$ overall': 'linearithmic',
    '$O(M\\log N)$ per test case': 'linearithmic',
    '$O((N+M+Q)\\alpha(N))$ per test case': 'near-linear',
    '$O(\\log\\max(i,j))$ per query': 'linearithmic',
    '$O(|S|)$ per test case to read the input; $O(1)$ to check its suffix': 'linear',
    '$O(\\sum N_i+M)$ per test case': 'linear',
    '$O((N+M)\\log N)$ overall': 'linearithmic',
    '$O(E\\log E+V^2)$ overall': 'graph-output',
})

TABLE.update({
    '$O(V\\log\\log V+\\pi(V)+K\\log\\pi(V)+\\sum N^2)$ overall for $K$ prime cells and maximum password $V$': 'near-linear',
    '$O(64+\\log N)$ per test case': 'log',
    '$O(M^3+NM^2)$ per test case': 'matrix-dp',
    '$O((K+2)N^2+2^K K^2)$ per test case for $K$ treasures': 'subset-dp',
    '$O((X+1)(M+1)(N+1))$ per test case': 'product',
    '$O(V\\log\\log V+T)$ overall for $V=\\max N$': 'near-linear',
    '$O(V\\log V+T)$ overall for $V=\\max R$': 'linearithmic',
    '$O(N\\pi(\\sqrt V))$ trial divisions per test case after a sieve to $\\sqrt V$': 'trial-factor',
    '$O(V\\log V+T\\sqrt V)$ overall for $V=\\max N$': 'linearithmic',
    '$O(V\\log\\log V+\\pi(V)^2+T)$ overall for $V=\\max N$': 'quadratic',
    '$O(\\sqrt N+\\log N)$ per test case': 'sqrt',
    '$O(V\\log\\log V+N+V\\sum_{p\\le V+1}1/p+\\pi(V+1))$ per test case': 'near-linear',
    '$O(V\\log\\log V+T)$ overall for $V=\\max X$': 'near-linear',
    '$O(V\\log\\log V+\\sum N)$ overall for fixed sieve bound $V=400000$': 'near-linear',
})

TABLE.update({
    '$O(S\\log S)$ per test case for $S=NM$': 'linearithmic',
    '$O(NW)$ per test case': 'product',
    '$O(NM/w)$ word operations per test case': 'bit-knapsack',
    '$O((N+M)\\log M+N\\log K+KB)$ per test case with $B\\le\\min(N,\\sum_{c=1}^{200}\\lfloor K/c\\rfloor)$': 'budget-dp',
    '$O(N^2+NI/w)$ word operations per test case for $I$ total inversions': 'bit-knapsack',
    '$O(N^2+ND/w)$ word operations per test case for $D\\le N^2/2$ total absolute imbalance': 'bit-knapsack',
    '$O(|S|^2)$ overall': 'quadratic',
    '$O(\\log N+\\log MOD)$ per test case': 'log',
    '$O(KU+N)$ per test case for $U=2\\max H$ and $K$ distinct fuel amounts': 'product',
    '$O(V+T)$ overall for $V=\\max N$': 'linear',
    '$O(N+M+AB/w)$ word operations per test case for compressed lengths $A,B$': 'product',
    '$O(|S|^2)$ per test case': 'quadratic',
})

# Later roadmap courses (1600-1800 remainder, 3* to 4*, 2000 to 2500).
TABLE.update({
    '$O(N^5)$ worst case per test case - $N$ Dinic runs on $O(N)$ vertices and $O(N^2)$ edges': 'high-poly',
    '$O(N \\cdot S / w)$ per test case, $S$ the sum of the values': 'bit-knapsack',
    '$O((NC+NQ+CY)Y/w)$ word operations per test case for $C=\\min(N,Y)$ and $Q$ an initial valid swap bound': 'bit-knapsack',
    '$O(N \\cdot K \\cdot S / w + N \\cdot S)$ per test case, $S$ the largest reachable sum': 'bit-knapsack',
    '$O(N \\cdot M)$': 'product',
    '$O(Q \\cdot N \\cdot M)$, with repeated query sizes answered from a cache': 'high-poly',
    '$O(N \\cdot M + (N + M) \\cdot K)$ per test case': 'product',
    '$O(A \\log \\log A + N \\log A)$ over the whole input, $A$ the largest value': 'near-linear',
    '$O(Q \\cdot B \\cdot P^2)$ with $P \\le 50$ topped slices and $B$ bits in the total sweetness': 'high-poly',
    '$O(N^2 L + K N^2)$ per test case': 'high-poly',
    '$O(N \\cdot A^2 \\cdot H)$ in the worst case over all states, $H$ the largest hash value': 'high-poly',
    '$O(N \\cdot \\min(N, L))$ per test case': 'quadratic',
    '$O(D \\cdot (N \\cdot D + D \\cdot 4^D))$ per test case, $D \\le 9$ digits': 'subset-dp',
    '$O(70 \\cdot \\max N + T)$': 'linear',
    '$O(2^N \\cdot N^2)$ in the worst case; pruning keeps the visited states far below that for $N \\le 30$': 'subset-dp',
    '$O(B_{\\max} + T \\cdot B)$': 'linear',
    '$O(\\max N + T)$': 'linear',
    '$O(60 \\cdot 2^{M} \\cdot M)$ worst case per test case with memoisation, $M \\le 15$': 'subset-dp',
    '$O(N + Q)$': 'linear',
    '$O(16 \\cdot N + Q)$': 'linear',
    '$O(N + P)$': 'linear',
    '$O((N + Q) \\log N)$': 'linearithmic',
    '$O(N_{\\max}^2 + \\sum \\min(N, M, K))$': 'quadratic',
    '$O(S + Q \\log Q + E \\log N)$, $S$ the total number of chocolates and $E = \\sum O(\\sqrt{count})$ breakpoints': 'linearithmic',
    '$O(\\max(N + M) + \\sum N)$': 'linear',
    '$O(p(n) \\cdot m^2)$, $n = \\min(N, M)$, $m = \\max(N, M)$ and $p$ the partition function': 'subset-dp',
    '$O(N \\sqrt{N})$': 'n-sqrt',
    '$O(N \\log N + D \\cdot B \\log N + Q (\\sqrt{N} + D))$ with $D = O(\\sqrt{N})$ branching depths and $B$ distinct anchors queried': 'n-sqrt',
    '$O(N)$ for $K = 1$; otherwise $O(N \\log K)$ plus $O(\\log N)$ levels of big-integer convolutions': 'n-polylog',
    '$O(N + \\log \\sum a_i)$ per test case': 'linear',
    '$O((N + M) \\log N + Q)$': 'linearithmic',
    '$O(\\min(D \\cdot P,\\; U \\log U))$ per test case with $D$ distinct values, $P$ palindromes below $U = 2^{15}$': 'linearithmic',
    '$O(\\log^2 B)$ per test case': 'polylog',
    '$O(\\sqrt{N} + Q \\cdot \\omega(N) \\log K)$': 'sqrt',
    '$O(N)$ per query': 'linear',
    '$O(N + C)$ per test case, $C = 10^5$': 'linear',
    '$O(\\max L + T)$': 'linear',
    '$O(\\log^2 (Y / X))$ per test case': 'polylog',
    '$O(\\sqrt{A} + \\sqrt{B})$ per uncached pair': 'sqrt',
    '$O(N \\cdot M \\cdot \\log \\max(N, M))$ per test case': 'linearithmic',
    '$O(1)$ expected per test case - a handful of iterations': 'constant',
    '$O(N \\log M)$ per test case plus the short downward searches': 'linearithmic',
    '$O(N^2)$ per test case with $N \\le 1000$': 'quadratic',
    '$O(N)$ per test case after $O(\\max N)$ precomputation': 'linear',
    '$O(M_{\\max} \\log \\log M_{\\max})$ sieve, then $O(N \\log A)$ per test case': 'linearithmic',
    '$O(N \\cdot M + Q)$': 'product',
    '$O(\\sqrt{V})$ precomputation and $O(1)$ per query, $V$ the largest label': 'constant',
    '$O(V \\log V + N \\cdot \\tau(V))$, $V$ the largest value': 'linearithmic',
    '$O(N \\log \\log N)$ sieve, then $O(N)$ per test case': 'linear',
    '$O(55)$ iterations per test case': 'constant',
    '$O(N \\cdot 2^N)$ per test case': 'subset-dp',
    '$O(D / 99998 + 1)$ per test case': 'linear',
    '$O(V \\log \\log V + N \\log V)$, $V$ the largest value': 'linearithmic',
    '$O(\\log \\max(A, B, C))$ per test case': 'log',
    '$O(100 \\cdot 2^N \\cdot N)$ per test case': 'subset-dp',
    '$O(S \\log S)$ per test case, $S$ the total number of ants': 'linearithmic',
    '$O(N + K \\log N)$': 'linearithmic',
    '$O(N)$ expected': 'linear',
    '$O((B + C) \\log (B + C))$ per test case': 'linearithmic',
    '$O(30 \\cdot N)$ per test case': 'linear',
    '$O(B + W)$ per test case': 'linear',
    '$O((N + M)\\,\\alpha(N))$ per test case after factorial precomputation': 'near-linear',
    '$O(30 \\cdot N + Q)$': 'linear',
    '$O(N \\cdot K)$ per test case': 'product',
    '$O(N + M)$ precomputation, $O(\\log (N M))$ per test case': 'log',
    '$O((N + M + Q) \\log (N + M + Q))$': 'linearithmic',
    '$O(Q)$': 'linear',
    '$O(N + M \\log M)$ per test case': 'linearithmic',
    '$O(N + M + \\log \\text{answer})$ per test case': 'linear',
    '$O(N + \\log K)$ per test case': 'linear',
    '$O(N + M + S \\log S)$ per test case': 'linearithmic',
    '$O(\\sqrt{x + y})$ per test case': 'sqrt',
    '$O(30 \\cdot N \\cdot \\alpha(N))$ per test case': 'near-linear',
    '$O(N + M)$ expected per test case': 'linear',
    '$O(N M \\log (N M))$ per test case': 'linearithmic',
    '$O(V \\log \\log V + (N + Q) \\log V \\log N)$': 'n-polylog',
    '$O(26 \\cdot N)$ per test case': 'linear',
    '$O(V \\log \\log V + N \\log V)$, $V$ the largest value in the input': 'linearithmic',
    '$O(\\log p)$ per test case': 'log',
    '$O(M \\log M + \\sum \\text{list lengths})$ per test case': 'linearithmic',
})

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
