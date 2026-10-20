#!/usr/bin/env python3
"""
Custom checkers for problems that accept more than one correct answer.

CodeChef judges these with a special checker, so comparing against the sample
output verbatim reports a false failure. Each entry here takes the sample input
and our output and decides whether the answer is acceptable.
"""
from fractions import Fraction


def _avgperm(inp, got):
    """AVGPERM: any permutation minimising the sum of triplet averages."""
    toks = inp.split()
    t = int(toks[0])
    sizes = [int(toks[1 + i]) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"

    def cost(p):
        return sum(Fraction(p[i] + p[i + 1] + p[i + 2], 3) for i in range(len(p) - 2))

    for n, line in zip(sizes, lines):
        p = list(map(int, line.split()))
        if sorted(p) != list(range(1, n + 1)):
            return False, f"n={n}: not a permutation of 1..{n}"
        # The optimum pairs the largest values with the smallest triplet
        # weights (1, 2, 3, ..., 3, 2, 1), so build that cost directly.
        weight = sorted(min(j, n - 2, n - j + 1, 3) for j in range(1, n + 1))
        values = sorted(range(1, n + 1), reverse=True)
        best = Fraction(sum(w * v for w, v in zip(weight, values)), 3)
        if cost(p) != best:
            return False, f"n={n}: cost {cost(p)} but optimum is {best}"
    return True, "optimal"


CHECKERS = {
    "AVGPERM": _avgperm,
}
