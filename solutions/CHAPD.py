import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        while b > 1:
            g = gcd(a, b)
            if g == 1:
                break                 # what is left shares no prime with A
            while b % g == 0:         # strip those primes to full multiplicity
                b //= g
        out.append("Yes" if b == 1 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
