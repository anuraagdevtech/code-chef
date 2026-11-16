import sys
from math import isqrt
from collections import Counter

def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime

PRIMES = [i for i,v in enumerate(sieve(1000)) if v]


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        exponents = Counter()
        for _ in range(n):
            value = int(next(tokens))
            for p in PRIMES:
                if p*p > value:
                    break
                while value%p == 0:
                    exponents[p] += 1
                    value //= p
            if value > 1:
                exponents[value] += 1
        answer = 1
        for exponent in exponents.values():
            answer *= exponent+1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
