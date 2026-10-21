import sys
from bisect import bisect_left, bisect_right
from math import isqrt

LIMIT = 10 ** 6 + 1          # sqrt of the largest R


def main() -> None:
    sieve = bytearray([1]) * LIMIT
    sieve[0:2] = b"\0\0"
    for p in range(2, isqrt(LIMIT) + 1):
        if sieve[p]:
            sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
    primes = [i for i in range(2, LIMIT) if sieve[i]]
    # d(p^e) = e + 1 must be prime; 2^40 already exceeds 10^12.
    exps = [e for e in range(4, 41) if sieve[e + 1]]

    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        lo, hi = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # e = 1: the primes in [lo, hi], by segmented sieve.
        window = bytearray([1]) * (hi - lo + 1)
        if lo == 1:
            window[0] = 0
        for p in primes:
            if p * p > hi:
                break
            start = max(p * p, (lo + p - 1) // p * p)
            if start <= hi:
                window[start - lo::p] = bytearray(len(window[start - lo::p]))
        total = sum(window)
        # e = 2: prime squares, counted in the base prime list.
        left, right = isqrt(lo - 1) + 1, isqrt(hi)
        if right >= left:
            total += bisect_right(primes, right) - bisect_left(primes, left)
        # e >= 4: only a handful of prime powers are small enough.
        for e in exps:
            for p in primes:
                v = p ** e
                if v > hi:
                    break
                if v >= lo:
                    total += 1
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
