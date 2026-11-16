import sys

from math import isqrt

LIMIT = 400000
prime = bytearray(b'\x01')*(LIMIT+1)
prime[0:2] = b'\x00\x00'
for p in range(2,isqrt(LIMIT)+1):
    if prime[p]:
        prime[p*p:LIMIT+1:p] = b'\x00'*((LIMIT-p*p)//p+1)
LARGE_PRIMES = [p for p in range(7,LIMIT+1) if prime[p]]


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        if n == 3:
            edge_primes = [2,3,5]
        else:
            even = n if n%2 == 0 else n-1
            count = even//2
            small = [2 if i%2 == 0 else 3 for i in range(count)]
            if small[-1] == small[0]:
                small[-1] = 5
            edge_primes = []
            for i in range(count):
                edge_primes.extend((small[i],LARGE_PRIMES[i]))
            if n%2:
                inserted = next(p for p in (2,3,5) if p != edge_primes[0] and p != edge_primes[2])
                edge_primes.insert(2,inserted)
        answer = [edge_primes[i]*edge_primes[(i+1)%n] for i in range(n)]
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
