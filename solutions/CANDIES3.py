import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    at_least = [0] * (m + 2)
    for _ in range(n):
        at_least[next(tokens)] += 1
    bonus = [next(tokens) for _ in range(m)]
    for i in range(m - 1, -1, -1):
        at_least[i] += at_least[i + 1]
    return str(max((bonus[price - 1] * sum((at_least[j] for j in range(price, m + 1, price))) for price in range(1, m + 1))))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
