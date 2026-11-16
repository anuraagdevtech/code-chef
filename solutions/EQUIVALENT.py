import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []

    def canonical(n):
        rest = n
        prime = 2
        factors = []
        common = 0
        while prime * prime <= rest:
            exponent = 0
            while rest % prime == 0:
                rest //= prime
                exponent += 1
            if exponent:
                factors.append((prime, exponent))
                common = gcd(common, exponent)
            prime = 3 if prime == 2 else prime + 2
        if rest > 1:
            factors.append((rest, 1))
            common = 1
        base = 1
        for prime, exponent in factors:
            base *= prime ** (exponent // common)
        return base
    cache = {}
    for _ in range(next(tokens)):
        a = next(tokens)
        b = next(tokens)
        if a not in cache:
            cache[a] = canonical(a)
        if b not in cache:
            cache[b] = canonical(b)
        out.append('YES' if cache[a] == cache[b] else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
