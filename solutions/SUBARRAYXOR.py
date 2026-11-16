import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        out.append(' '.join((str(i ^ i - 1) for i in range(1, n + 1))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
