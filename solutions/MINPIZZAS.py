import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # K already supplies gcd(n, k) of the factor n, so P covers the rest.
        out.append(str(n // gcd(n, k)))
    sys.stdout.write("\n".join(out) + "\n")


main()
