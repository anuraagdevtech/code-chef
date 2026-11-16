import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    q = next(tokens)
    rest = n
    factors = []
    prime = 2
    while prime * prime <= rest:
        exponent = 0
        while rest % prime == 0:
            rest //= prime
            exponent += 1
        if exponent:
            factors.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if rest > 1:
        factors.append((rest, 1))
    total = 1
    for prime, exponent in factors:
        total *= exponent + 1
    out = []
    for _ in range(q):
        kind = next(tokens)
        k = next(tokens)
        if kind == 1:
            k = gcd(n, k)
            answer = 1
            for prime, exponent in factors:
                power = 0
                while k % prime == 0:
                    k //= prime
                    power += 1
                answer *= power + 1
        else:
            answer = 0
            if n % k == 0:
                answer = 1
                for prime, exponent in factors:
                    power = 0
                    while k % prime == 0:
                        k //= prime
                        power += 1
                    answer *= exponent - power + 1
            if kind == 3:
                answer = total - answer
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
