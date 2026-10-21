import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        lcm = x // gcd(x, y) * y
        # XY - X - Y solves both congruences; shift it into (0, lcm].
        n = (x * y - x - y) % lcm
        out.append(str(n if n else lcm))
    sys.stdout.write("\n".join(out) + "\n")


main()
