import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    MOD = 10 ** 9 + 7
    for _ in range(next(tokens)):
        bits = next(tokens).bit_count()
        out.append(str((pow(3, bits, MOD) - 3 * pow(2, bits, MOD) + 3) % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
