import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = sorted((next(tokens) for _ in range(n)))
        arranged = [0] * n
        arranged[::2] = values[:(n + 1) // 2][::-1]
        arranged[1::2] = values[(n + 1) // 2:][::-1]
        ok = all((arranged[i - 1] < arranged[i] > arranged[i + 1] or arranged[i - 1] > arranged[i] < arranged[i + 1] for i in range(1, n - 1)))
        if not ok:
            arranged[::2] = values[n // 2:]
            arranged[1::2] = values[:n // 2]
            ok = all((arranged[i - 1] < arranged[i] > arranged[i + 1] or arranged[i - 1] > arranged[i] < arranged[i + 1] for i in range(1, n - 1)))
        out.append(' '.join(map(str, arranged)) if ok else '-1')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
