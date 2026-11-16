import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    n = next(tokens)
    m = next(tokens)
    q = next(tokens)
    for _ in range(q):
        target = next(tokens)
        rows = 1
        while m * rows * (rows + 1) // 2 < target:
            rows += 1
        extra = target - rows * (rows + 1) // 2
        lengths = [1] * rows
        for i in range(rows, 0, -1):
            more = min(m - 1, extra // i)
            lengths[i - 1] += more
            extra -= i * more
        out.append(f'1 {rows}')
        out.append(' '.join(map(str, lengths)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
