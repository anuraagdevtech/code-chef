import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        best = x                               # walk the whole way
        # Largest k with k(k+1)/2 <= x, from inverting the triangular formula.
        k0 = (math.isqrt(8 * x + 1) - 1) // 2
        # Cost is unimodal in k, so only the stations bracketing x matter.
        for k in range(max(1, k0 - 1), k0 + 3):
            best = min(best, k + abs(x - k * (k + 1) // 2))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
