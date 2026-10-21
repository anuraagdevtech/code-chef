import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        gap = abs(a - b)
        if gap == 0:
            out.append("-1")          # every p works
            continue
        # p works iff p divides the difference, so count its divisors.
        count = 0
        for d in range(1, isqrt(gap) + 1):
            if gap % d == 0:
                count += 1 if d * d == gap else 2
        out.append(str(count))
    sys.stdout.write("\n".join(out) + "\n")


main()
