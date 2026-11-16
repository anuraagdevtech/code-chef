import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        a = next(tokens)
        b = next(tokens)
        while b > 1:
            common = gcd(a, b)
            if common == 1:
                break
            b //= common
        out.append('YES' if b == 1 else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
