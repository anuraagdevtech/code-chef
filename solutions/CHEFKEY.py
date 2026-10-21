import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m, c = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        found = 0
        for d in range(1, isqrt(c) + 1):
            if c % d:
                continue
            other = c // d
            if d <= n and other <= m:
                found += 1
            # The mirrored orientation is a separate section unless d == c/d.
            if other != d and other <= n and d <= m:
                found += 1
        out.append(str(found))
    sys.stdout.write("\n".join(out) + "\n")


main()
