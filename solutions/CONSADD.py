import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        rows = next(tokens)
        cols = next(tokens)
        width = next(tokens)
        delta = [[next(tokens) for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                delta[i][j] -= next(tokens)
        for row in delta:
            diff = [0] * (cols + 1)
            applied = 0
            for j in range(cols):
                applied += diff[j]
                v = row[j] + applied
                if j + width <= cols:
                    applied -= v
                    diff[j + width] += v
                    row[j] = 0
                else:
                    row[j] = v
        ok = True
        for j in range(cols - width + 1, cols):
            diff = [0] * (rows + 1)
            applied = 0
            for i in range(rows):
                applied += diff[i]
                v = delta[i][j] + applied
                if i + width <= rows:
                    applied -= v
                    diff[i + width] += v
                elif v:
                    ok = False
        out.append('YES' if ok else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
