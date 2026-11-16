import sys
from bisect import bisect_left


def solve(tokens):
    n, chef = (next(tokens), next(tokens))
    officers = sorted((next(tokens) for _ in range(n)))
    split = bisect_left(officers, chef)
    eliminated = 0
    for i in range(split - 1, -1, -1):
        if (officers[i] - chef) % 2 == 0:
            break
        eliminated += 1
    for i in range(split, n):
        if (officers[i] - chef) % 2 == 0:
            break
        eliminated += 1
    return str(eliminated) + ' ' + ('1' if eliminated == n else '-1')


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
