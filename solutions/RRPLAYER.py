import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    queries = [next(tokens) for _ in range(next(tokens))]
    harmonic = [0.0] * (max(queries, default=0) + 1)
    for i in range(1, len(harmonic)):
        harmonic[i] = harmonic[i - 1] + 1 / i
    print('\n'.join(('%.10f' % (n * harmonic[n]) for n in queries)))


if __name__ == "__main__":
    main()
