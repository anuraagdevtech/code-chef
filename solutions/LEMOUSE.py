import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, m = (int(next(tokens)), int(next(tokens)))
        board = [next(tokens) for _ in range(n)]

        def near(x, y):
            return {(u, v) for u, v in ((x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if 0 <= u < n and 0 <= v < m}
        best = [[[10 ** 9] * 2 for _ in range(m)] for _ in range(n)]
        initial = sum((board[x][y] == 49 for x, y in near(0, 0)))
        best[0][0] = [initial, initial]
        for x in range(n):
            for y in range(m):
                for last in range(2):
                    if best[x][y][last] >= 10 ** 9:
                        continue
                    seen = near(x, y)
                    if x + y:
                        seen |= near(x - (last == 0), y - (last == 1))
                    for d, (u, v) in enumerate(((x + 1, y), (x, y + 1))):
                        if u < n and v < m:
                            best[u][v][d] = min(best[u][v][d], best[x][y][last] + sum((board[r][s] == 49 for r, s in near(u, v) - seen)))
        out.append(str(min(best[-1][-1])))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
