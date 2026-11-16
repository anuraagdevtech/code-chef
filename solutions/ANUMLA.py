import sys
from collections import Counter


def solve(tokens):
    n = next(tokens)
    sums_sorted = sorted((next(tokens) for _ in range(1 << n)))
    remaining = Counter(sums_sorted)
    remaining[0] -= 1
    sums = [0]
    found = []
    for value in sums_sorted:
        if remaining[value]:
            found.append(value)
            new = [v + value for v in sums]
            for v in new:
                remaining[v] -= 1
            sums += new
    return ' '.join(map(str, found))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
