import sys
from array import array


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [[next(tokens) for _ in range(next(tokens))] for _ in range(next(tokens))]
    limit = max(map(max, cases), default=1)
    spf = array('I', [0]) * (limit + 1)
    for prime in range(2, int(limit ** 0.5) + 1):
        if not spf[prime]:
            for x in range(prime * prime, limit + 1, prime):
                if not spf[x]:
                    spf[x] = prime
    out = []
    for rooms in cases:
        best_for_prime = {}
        answer = 1
        for x in rooms:
            factors = []
            while x > 1:
                prime = spf[x] or x
                factors.append(prime)
                while x % prime == 0:
                    x //= prime
            length = 1 + max((best_for_prime.get(prime, 0) for prime in factors), default=0)
            for prime in factors:
                best_for_prime[prime] = length
            answer = max(answer, length)
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
