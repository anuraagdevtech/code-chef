import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a1, d = int(data[1 + 4 * i]), int(data[2 + 4 * i])
        l, r = int(data[3 + 4 * i]), int(data[4 + 4 * i])
        step = d % 9
        # Reduce first: (L - 1) * D would otherwise reach 10^27.
        start = (a1 + (l - 1) % 9 * step) % 9
        period = 9 // gcd(step, 9) if step else 1
        roots = []
        cur = start
        for _ in range(period):
            roots.append(cur if cur else 9)
            cur = (cur + step) % 9
        n = r - l + 1
        total = n // period * sum(roots) + sum(roots[:n % period])
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
