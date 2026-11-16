import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        a = next(tokens)
        b = next(tokens)
        c = next(tokens)
        out.append(str(1 << (a ^ b).bit_count()))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
