import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if gcd(x, y) > 1:
            out.append("0")
        elif x % 2 == 0 or y % 2 == 0:
            # Coprime with one even member: bump the odd one and share 2.
            out.append("1")
        elif gcd(x + 1, y) > 1 or gcd(x, y + 1) > 1:
            out.append("1")
        else:
            out.append("2")          # both +1 always shares the factor 2
    sys.stdout.write("\n".join(out) + "\n")


main()
