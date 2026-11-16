import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        values = [next(tokens) for _ in range(n)]
        ok = values == values[::-1] if n == k else n % 2 == 1 or k % 2 == 1 or sum(values) % 2 == 0
        out.append('YES' if ok else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
