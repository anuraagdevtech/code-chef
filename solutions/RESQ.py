import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # N/d - d falls as d rises, so the largest divisor below sqrt(N) wins.
        best = 1
        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                best = d
        out.append(str(n // best - best))
    sys.stdout.write("\n".join(out) + "\n")


main()
