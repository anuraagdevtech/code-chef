import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n = int(next(tokens))
    m = int(next(tokens))
    grid = [next(tokens) for _ in range(n)]
    diff = [bytearray(m + 1) for _ in range(n + 1)]
    for _ in range(int(next(tokens))):
        x = int(next(tokens)) - 1
        y = int(next(tokens)) - 1
        u = int(next(tokens))
        v = int(next(tokens))
        diff[x][y] ^= 1
        diff[x][v] ^= 1
        diff[u][y] ^= 1
        diff[u][v] ^= 1
    out = []
    for i in range(n):
        run = 0
        row = diff[i]
        above = diff[i - 1] if i else bytearray(m + 1)
        line = []
        for j in range(m):
            run ^= row[j]
            row[j] = run ^ above[j]
            line.append(str(grid[i][j] - 48 ^ row[j]))
        out.append(''.join(line))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
