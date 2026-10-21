import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # gcd(0, x) == x, so sorted positions impose no constraint.
        step = 0
        for i in range(n):
            step = gcd(step, abs(int(data[pos + 1 + i]) - (i + 1)))
        pos += 1 + n
        out.append(str(step))
    sys.stdout.write("\n".join(out) + "\n")


main()
