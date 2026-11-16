import sys
from math import gcd


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, a, k = (int(next(tokens)) for _ in range(3))
        den = n*(n-1)
        num = a*den + 2*(k-1)*(180*(n-2)-n*a)
        g = gcd(abs(num), den)
        out.append(f'{num//g} {den//g}')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
