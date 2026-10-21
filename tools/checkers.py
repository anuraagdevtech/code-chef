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


def _n1values(inp, got):
    """N1VALUES: N+1 positive ints, one repeated, summing to 2**N, sorted."""
    toks = inp.split()
    t = int(toks[0])
    sizes = [int(toks[1 + i]) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for n, line in zip(sizes, lines):
        a = list(map(int, line.split()))
        if len(a) != n + 1:
            return False, f"n={n}: expected {n+1} values, got {len(a)}"
        if any(v <= 0 for v in a):
            return False, f"n={n}: values must be positive"
        if a != sorted(a):
            return False, f"n={n}: not non-decreasing"
        if sum(a) != 1 << n:
            return False, f"n={n}: sum {sum(a)} != 2^{n}"
        from collections import Counter
        c = Counter(a)
        twice = [v for v, k in c.items() if k == 2]
        if len(twice) != 1 or any(k > 2 for k in c.values()):
            return False, f"n={n}: exactly one value must appear twice"
    return True, "valid"


def _gcdsubarrays(inp, got):
    """GCDSUBARRAYS: array whose subarray-gcd total is K, or -1."""
    from math import gcd
    toks = inp.split()
    t = int(toks[0])
    cases = [(int(toks[1 + 2 * i]), int(toks[2 + 2 * i])) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for (n, k), line in zip(cases, lines):
        if line.strip() == "-1":
            if k >= n * (n + 1) // 2:
                return False, f"n={n},k={k}: claimed impossible but is not"
            continue
        a = list(map(int, line.split()))
        if len(a) != n:
            return False, f"n={n}: wrong length"
        if any(v < 1 or v > 10 ** 18 for v in a):
            return False, f"n={n}: value out of range"
        total = 0
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, a[j])
                total += g
        if total != k:
            return False, f"n={n}: gcd total {total} != {k}"
    return True, "valid"


def _palinpain(inp, got):
    """PALINPAIN: two distinct palindromes with exactly X 'a' and Y 'b', or -1."""
    toks = inp.split()
    t = int(toks[0])
    cases = [(int(toks[1 + 2 * i]), int(toks[2 + 2 * i])) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    idx = 0
    for x, y in cases:
        if idx >= len(lines):
            return False, "ran out of output"
        if lines[idx].strip() == "-1":
            # Impossible iff both counts are odd, or either is below 2.
            if not ((x % 2 and y % 2) or x < 2 or y < 2):
                return False, f"X={x},Y={y}: claimed impossible but is not"
            idx += 1
            continue
        s1, s2 = lines[idx], lines[idx + 1]
        idx += 2
        if s1 == s2:
            return False, f"X={x},Y={y}: the two strings are identical"
        for s in (s1, s2):
            if s != s[::-1]:
                return False, f"X={x},Y={y}: {s} is not a palindrome"
            if s.count("a") != x or s.count("b") != y or len(s) != x + y:
                return False, f"X={x},Y={y}: {s} has the wrong letter counts"
    return True, "valid"


def _prefperm(inp, got):
    """PREFPERM: a permutation whose permutation-prefixes are exactly A."""
    toks = inp.split()
    t = int(toks[0])
    pos = 1
    cases = []
    for _ in range(t):
        n, k = int(toks[pos]), int(toks[pos + 1])
        a = [int(v) for v in toks[pos + 2:pos + 2 + k]]
        pos += 2 + k
        cases.append((n, a))
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for (n, a), line in zip(cases, lines):
        p = list(map(int, line.split()))
        if sorted(p) != list(range(1, n + 1)):
            return False, f"n={n}: not a permutation"
        # A prefix is a permutation exactly when its running max equals its length.
        run_max = 0
        found = []
        for i, v in enumerate(p, 1):
            run_max = max(run_max, v)
            if run_max == i:
                found.append(i)
        if found != a:
            return False, f"n={n}: permutation prefixes {found} != {a}"
    return True, "valid"


def _chsqr(inp, got):
    """CHSQR: a K x K Latin square whose nearest 1 to the centre is at (K-1)/2."""
    toks = inp.split()
    t = int(toks[0])
    sizes = [int(toks[1 + i]) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    idx = 0
    for k in sizes:
        if idx + k > len(lines):
            return False, f"k={k}: not enough rows"
        grid = [list(map(int, lines[idx + r].split())) for r in range(k)]
        idx += k
        want = set(range(1, k + 1))
        for r in range(k):
            if len(grid[r]) != k or set(grid[r]) != want:
                return False, f"k={k}: row {r} is not a permutation of 1..{k}"
        for c in range(k):
            if set(grid[r][c] for r in range(k)) != want:
                return False, f"k={k}: column {c} is not a permutation of 1..{k}"
        mid = (k - 1) // 2
        best = min(abs(r - mid) + abs(c - mid)
                   for r in range(k) for c in range(k) if grid[r][c] == 1)
        if best != (k - 1) // 2:
            return False, f"k={k}: nearest 1 at {best}, optimum is {(k - 1) // 2}"
    return True, "optimal"


def _orandcon(inp, got):
    """ORANDCON: distinct A,B,C <= 1e9 with (A|B)&(B|C)&(C|A) == X."""
    toks = inp.split()
    t = int(toks[0])
    xs = [int(toks[1 + i]) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for x, line in zip(xs, lines):
        a, b, c = map(int, line.split())
        if len({a, b, c}) != 3:
            return False, f"X={x}: values not distinct"
        if any(v < 0 or v > 10 ** 9 for v in (a, b, c)):
            return False, f"X={x}: value out of [0, 1e9]"
        if (a | b) & (b | c) & (c | a) != x:
            return False, f"X={x}: expression gives {(a | b) & (b | c) & (c | a)}"
    return True, "valid"


def _ammeat2(inp, got):
    """AMMEAT2: K plates from 1..N, pairwise non-coprime, or -1."""
    from math import gcd
    toks = inp.split()
    t = int(toks[0])
    cases = [(int(toks[1 + 2 * i]), int(toks[2 + 2 * i])) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for (n, k), line in zip(cases, lines):
        vals = list(map(int, line.split()))
        if vals == [-1]:
            if k == 1 or 2 * k <= n:
                return False, f"n={n},k={k}: claimed impossible but is not"
            continue
        if len(vals) != k or len(set(vals)) != k:
            return False, f"n={n},k={k}: need {k} distinct plates"
        if any(v < 1 or v > n for v in vals):
            return False, f"n={n},k={k}: plate out of range"
        for x in range(len(vals)):
            for y in range(x + 1, len(vals)):
                if gcd(vals[x], vals[y]) == 1:
                    return False, f"n={n}: {vals[x]} and {vals[y]} are coprime"
    return True, "valid"


def _divcol(inp, got):
    """DIVCOL: minimal C and a valid colouring of the divisibility order."""
    toks = inp.split()
    t = int(toks[0])
    sizes = [int(toks[1 + i]) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    idx = 0
    for n in sizes:
        c = int(lines[idx]); idx += 1
        a = list(map(int, lines[idx].split())); idx += 1
        if c != n.bit_length():
            return False, f"n={n}: C={c}, optimum is {n.bit_length()}"
        if len(a) != n or any(v < 1 or v > c for v in a):
            return False, f"n={n}: values outside 1..{c}"
        for x in range(1, n + 1):
            for y in range(2 * x, n + 1, x):
                if a[x - 1] == a[y - 1]:
                    return False, f"n={n}: {x} divides {y} but colours match"
    return True, "optimal"


def _advitiya5(inp, got):
    """ADVITIYA5: a permutation with exactly K odd adjacent sums."""
    toks = inp.split()
    t = int(toks[0])
    cases = [(int(toks[1 + 2 * i]), int(toks[2 + 2 * i])) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for (n, k), line in zip(cases, lines):
        p = list(map(int, line.split()))
        if sorted(p) != list(range(1, n + 1)):
            return False, f"n={n}: not a permutation"
        odd = sum(1 for i in range(n - 1) if (p[i] + p[i + 1]) % 2)
        if odd != k:
            return False, f"n={n}: {odd} odd sums, wanted {k}"
    return True, "valid"


def _makediv3(inp, got):
    """MAKEDIV3: an N-digit odd number divisible by 3 but not 9, no leading zero."""
    toks = inp.split()
    t = int(toks[0])
    sizes = [int(toks[1 + i]) for i in range(t)]
    lines = [ln.strip() for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for n, s in zip(sizes, lines):
        if len(s) != n:
            return False, f"n={n}: wrong digit count {len(s)}"
        if s[0] == "0":
            return False, f"n={n}: leading zero"
        if int(s[-1]) % 2 == 0:
            return False, f"n={n}: not odd"
        ds = sum(int(c) for c in s)
        if ds % 3 or ds % 9 == 0:
            return False, f"n={n}: digit sum {ds} is not 3-but-not-9"
    return True, "valid"


def _indiperm(inp, got):
    """INDIPERM: a permutation with i not dividing P_i for every i >= 2."""
    toks = inp.split()
    t = int(toks[0])
    sizes = [int(toks[1 + i]) for i in range(t)]
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for n, line in zip(sizes, lines):
        p = list(map(int, line.split()))
        if sorted(p) != list(range(1, n + 1)):
            return False, f"n={n}: not a permutation"
        for i in range(2, n + 1):
            if p[i - 1] % i == 0:
                return False, f"n={n}: index {i} divides {p[i - 1]}"
    return True, "valid"


def _cntdist(inp, got):
    """CNTDIST: the sample masks line 1 with '*', so check both lines directly."""
    toks = inp.split()
    n = int(toks[0])
    want = len(set(toks[1:1 + n]))
    lines = [ln.strip() for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != 2:
        return False, f"expected 2 lines, got {len(lines)}"
    if lines[0] != "2":
        return False, f"complexity exponent {lines[0]}, should be 2"
    if lines[1] != str(want):
        return False, f"distinct count {lines[1]}, should be {want}"
    return True, "valid"


def _xorored(inp, got):
    """XORORED: any X attaining the minimum OR is accepted."""
    toks = inp.split()
    t = int(toks[0])
    pos = 1
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for line in lines:
        n = int(toks[pos])
        a = [int(x) for x in toks[pos + 1:pos + 1 + n]]
        pos += 1 + n
        parts = line.split()
        if len(parts) != 2:
            return False, f"expected 'X OR', got {line!r}"
        x, claimed = int(parts[0]), int(parts[1])
        if x < 0:
            return False, "X must be non-negative"
        # Mixed bits survive whatever X does, so this is the floor.
        best = 0
        for v in a:
            best |= v
        both = a[0]
        for v in a:
            both &= v
        best ^= both
        actual = 0
        for v in a:
            actual |= v ^ x
        if actual != best:
            return False, f"X={x} gives OR {actual}, optimum is {best}"
        if claimed != best:
            return False, f"reported OR {claimed} but optimum is {best}"
    return True, "optimal"


def _lisdigit(inp, got):
    """LISDIGIT: any n-digit number realising the given LIS array."""
    toks = inp.split()
    t = int(toks[0])
    pos = 1
    lines = [ln for ln in got.strip().splitlines() if ln.strip()]
    if len(lines) != t:
        return False, f"expected {t} lines, got {len(lines)}"
    for line in lines:
        n = int(toks[pos])
        want = [int(x) for x in toks[pos + 1:pos + 1 + n]]
        pos += 1 + n
        num = line.strip()
        if len(num) != n or not num.isdigit():
            return False, f"{num!r} is not a {n}-digit number"
        if n > 1 and num[0] == "0":
            return False, f"{num} has a leading zero"
        digits = [int(ch) for ch in num]
        lis = []
        for i, d in enumerate(digits):
            best = 0
            for j in range(i):
                if digits[j] < d and lis[j] > best:
                    best = lis[j]
            lis.append(best + 1)
        if lis != want:
            return False, f"{num} has LIS array {lis}, wanted {want}"
    return True, "valid"


CHECKERS = {
    "AVGPERM": _avgperm,
    "AVGARR": _avgarr,
    "PERMXORITY": _permxority,
    "CHDOGS": _float_tolerance(),
    "XOR_ORDER": _xor_order,
    "ALTERNATEDIV": _alternatediv,
    "N1VALUES": _n1values,
    "PALINPAIN": _palinpain,
    "PREFPERM": _prefperm,
    "CHSQR": _chsqr,
    "ORANDCON": _orandcon,
    "AMMEAT2": _ammeat2,
    "DIVCOL": _divcol,
    "ADVITIYA5": _advitiya5,
    "MAKEDIV3": _makediv3,
    "INDIPERM": _indiperm,
    "CNTDIST": _cntdist,
    "GCDSUBARRAYS": _gcdsubarrays,
    "XORORED": _xorored,
    "LISDIGIT": _lisdigit,
}
