import sys
from math import gcd,isqrt


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        r = isqrt(n)
        numerator = 2*sum(n//i for i in range(1,r+1))-r*r
        denominator = n*n
        g = gcd(numerator,denominator)
        out.append(f'{numerator//g}/{denominator//g}')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
