import sys
from math import gcd, isqrt


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    LIMIT = 1000000
    spf = list(range(LIMIT + 1))
    primes = []
    for i in range(2, LIMIT + 1):
        if spf[i] == i:
            primes.append(i)
            if i <= 1000:
                for j in range(i * i, LIMIT + 1, i):
                    if spf[j] == j:
                        spf[j] = i
    for _ in range(next(tokens)):
        n = next(tokens)
        m = next(tokens)
        values = [next(tokens) for _ in range(n)]
        if min(values) == max(values):
            out.append('0')
            continue
        common = 0
        for x in values:
            common = gcd(common, x)
        if common > 1:
            out.extend(['1', str(common)])
            continue
        used_primes = set()
        for x in set(values):
            while x > 1:
                prime = spf[x]
                used_primes.add(prime)
                while x % prime == 0:
                    x //= prime
        prime = next((prime for prime in primes if prime not in used_primes))
        if prime <= m:
            out.extend(['1', str(prime)])
        else:
            out.extend(['2', '2 3'])
    print('\n'.join(out))


if __name__ == "__main__":
    main()
