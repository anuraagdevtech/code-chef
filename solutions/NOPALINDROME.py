import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        period = k + 2 + (k - 1) // 2
        blocks, tail = divmod(n, period)
        out.append(str(3 * blocks + (3 if tail > k + 1 else 1 if tail else 0)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
