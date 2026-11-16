import sys
from collections import deque


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = (next(tokens), next(tokens))
    grid = [[next(tokens) for _ in range(m)] for _ in range(n)]
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        total = 0
        for j in range(m):
            total += grid[i][j]
            prefix[i + 1][j + 1] = prefix[i][j + 1] + total
    out = []
    cache = {}
    for _ in range(next(tokens)):
        height, width = (next(tokens), next(tokens))
        if (height, width) not in cache:
            horizontal = []
            for row in grid:
                window = deque()
                row_maxima = []
                for j, x in enumerate(row):
                    while window and row[window[-1]] <= x:
                        window.pop()
                    window.append(j)
                    while window[0] <= j - width:
                        window.popleft()
                    if j >= width - 1:
                        row_maxima.append(row[window[0]])
                horizontal.append(row_maxima)
            best = 10 ** 30
            for j in range(m - width + 1):
                window = deque()
                for i in range(n):
                    x = horizontal[i][j]
                    while window and horizontal[window[-1]][j] <= x:
                        window.pop()
                    window.append(i)
                    while window[0] <= i - height:
                        window.popleft()
                    if i >= height - 1:
                        top = i - height + 1
                        total = prefix[i + 1][j + width] - prefix[top][j + width] - prefix[i + 1][j] + prefix[top][j]
                        best = min(best, height * width * horizontal[window[0]][j] - total)
            cache[height, width] = best
        out.append(str(cache[height, width]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
