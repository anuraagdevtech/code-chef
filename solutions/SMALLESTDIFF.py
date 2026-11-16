import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    values = sorted((next(tokens) for _ in range(n * m)))
    transpose = n > m
    if transpose:
        n, m = (m, n)
    length = n + m - 1
    need_small = n // 2
    need_large = (n - 1) // 2
    start = min(range(need_small, len(values) - length - need_large + 1), key=lambda j: values[j + length - 1] - values[j])
    path = values[start:start + length]
    small = values[:start]
    large = values[start + length:]
    grid = [[0] * m for _ in range(n)]
    cursor = 0
    for i in range(n):
        grid[i][0] = path[cursor]
        cursor += 1
    for j in range(1, m):
        grid[n - 1][j] = path[cursor]
        cursor += 1
    for i in range(n - 1):
        grid[i][1] = small.pop() if i % 2 == 0 else large.pop()
    rest = iter(small + large)
    for i in range(n):
        for j in range(m):
            if not grid[i][j]:
                grid[i][j] = next(rest)
    if transpose:
        grid = [list(row) for row in zip(*grid)]
    return '\n'.join((' '.join(map(str, row)) for row in grid))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cursor = int(next(tokens))
    out = [solve(tokens) for _ in range(cursor)]
    sys.stdout.write('\n'.join(out))
