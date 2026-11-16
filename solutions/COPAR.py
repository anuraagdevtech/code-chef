import sys


spf = list(range(100001))
for i in range(2, 317):
    if spf[i] == i:
        for j in range(i * i, 100001, i):
            if spf[j] == j:
                spf[j] = i


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    last = {}
    factor_lists = []
    for i, value in enumerate(values):
        primes = []
        while value > 1:
            prime = spf[value]
            primes.append(prime)
            while value % prime == 0:
                value //= prime
        factor_lists.append(primes)
        for prime in primes:
            last[prime] = i
    end = 0
    for i, primes in enumerate(factor_lists):
        for prime in primes:
            end = max(end, last[prime])
        if i == end:
            return str(i + 1)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
