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


def _avgarr(inp, got):
    """AVGARR: any array of N distinct ints in [-1000, 1000] with mean X."""
    toks = inp.split()
    t = int(toks[0])
    cases = [(int(toks[1 + 2 * i]), int(toks[2 + 2 * i])) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for (n, x), line in zip(cases, lines):
        a = list(map(int, line.split()))
        if len(a) != n:
            return False, f"n={n}: wrong length {len(a)}"
        if len(set(a)) != n:
            return False, f"n={n}: values not distinct"
        if any(v < -1000 or v > 1000 for v in a):
            return False, f"n={n}: value out of [-1000, 1000]"
        if sum(a) != n * x:
            return False, f"n={n}: mean is not {x}"
    return True, "valid"


def _permxority(inp, got):
    """PERMXORITY: any permutation whose adjacent-difference XOR is zero."""
    toks = inp.split()
    t = int(toks[0])
    sizes = [int(toks[1 + i]) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for n, line in zip(sizes, lines):
        vals = line.split()
        if vals == ["-1"]:
            # Only n = 2 genuinely has no attractive permutation.
            if n != 2:
                return False, f"n={n}: claimed impossible, but a solution exists"
            continue
        p = list(map(int, vals))
        if sorted(p) != list(range(1, n + 1)):
            return False, f"n={n}: not a permutation of 1..{n}"
        x = 0
        for i in range(n - 1):
            x ^= abs(p[i] - p[i + 1])
        if x != 0:
            return False, f"n={n}: difference XOR is {x}, not 0"
    return True, "attractive"


def _float_tolerance(tol=1e-6):
    """Judge numerically: accept within absolute OR relative tolerance."""
    def check(inp, got):
        want_vals = check.expected
        got_vals = got.split()
        if len(got_vals) != len(want_vals):
            return False, f"expected {len(want_vals)} numbers, got {len(got_vals)}"
        for w, g in zip(want_vals, got_vals):
            wf, gf = float(w), float(g)
            if abs(wf - gf) <= tol or (wf and abs(wf - gf) / abs(wf) <= tol):
                continue
            return False, f"{gf} vs expected {wf}"
        return True, "within tolerance"
    return check


def _xor_order(inp, got):
    """XOR_ORDER: any X with (A^X) < (B^X) < (C^X), or -1 when none exists."""
    toks = inp.split()
    t = int(toks[0])
    cases = [tuple(int(toks[1 + 3 * i + k]) for k in range(3)) for i in range(t)]
    vals = got.split()
    if len(vals) != t:
        return False, f"expected {t} values, got {len(vals)}"
    for (a, b, c), v in zip(cases, vals):
        x = int(v)
        if x == -1:
            # Impossible exactly when both pairs turn on the same bit.
            if (a ^ b).bit_length() != (b ^ c).bit_length():
                return False, f"({a},{b},{c}): claimed impossible, but a solution exists"
            continue
        if not 0 <= x < (1 << 30):
            return False, f"({a},{b},{c}): X={x} out of range"
        if not ((a ^ x) < (b ^ x) < (c ^ x)):
            return False, f"({a},{b},{c}): X={x} does not order them"
    return True, "valid"


def _alternatediv(inp, got):
    """ALTERNATEDIV: any distinct array in [1, 2N] with alternating divisibility."""
    toks = inp.split()
    t = int(toks[0])
    sizes = [int(toks[1 + i]) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for n, line in zip(sizes, lines):
        a = list(map(int, line.split()))
        if len(a) != n:
            return False, f"n={n}: wrong length"
        if len(set(a)) != n:
            return False, f"n={n}: values not distinct"
        if any(v < 1 or v > 2 * n for v in a):
            return False, f"n={n}: value outside [1, {2 * n}]"
        for i in range(n - 1):            # i is 0-based; position is i + 1
            divides = a[i + 1] % a[i] == 0
            if (i + 1) % 2 == 1 and not divides:
                return False, f"n={n}: A[{i+1}] should divide A[{i+2}]"
            if (i + 1) % 2 == 0 and divides:
                return False, f"n={n}: A[{i+1}] should not divide A[{i+2}]"
    return True, "valid"


CHECKERS = {
    "AVGPERM": _avgperm,
    "AVGARR": _avgarr,
    "PERMXORITY": _permxority,
    "CHDOGS": _float_tolerance(),
    "XOR_ORDER": _xor_order,
    "ALTERNATEDIV": _alternatediv,
}
