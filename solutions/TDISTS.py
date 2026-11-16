import sys
from math import isqrt


def solve(tokens):
    x, y = (next(tokens), next(tokens))
    n = isqrt(x + y)
    gap = isqrt(max(0, x - y))
    if n * n != x + y or x < y or gap * gap != x - y or (n - gap) % 2:
        return 'NO'
    part_a = (n + gap) // 2
    part_b = n - part_a
    if part_b == 0:
        return 'NO'
    edges = ['1 ' + str(i) for i in range(part_a + 1, n + 1)] + [str(part_a + 1) + ' ' + str(i) for i in range(2, part_a + 1)]
    return 'YES\n' + str(n) + '\n' + '\n'.join(edges)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
