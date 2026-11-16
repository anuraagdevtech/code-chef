import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        block_col = [0] * n
        for _ in range(n):
            x = next(tokens) - 1
            y = next(tokens)
            block_col[x] = y
        ok = True
        upper = lower = False
        for i, col in enumerate(block_col):
            if i == 0 or abs(col - block_col[i - 1]) != 1:
                upper = lower = False
            upper = upper or i == 0 or col == n
            lower = lower or i == n - 1 or col == 1
            if upper and lower:
                ok = False
        out.append('YES' if ok else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
