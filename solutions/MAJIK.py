import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        merges = next(tokens)
        splits = next(tokens)
        values = sorted((next(tokens) for _ in range(n)))
        magnitudes = sorted((abs(x) for x in values[1:-1]), reverse=True)
        out.append(str(values[-1] - values[0] + sum(magnitudes[:merges + splits])))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
