import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        d = x - y
        # Smallest k with k(k+1)/2 >= d, from the quadratic root.
        k = (math.isqrt(8 * d + 1) - 1) // 2
        while k * (k + 1) // 2 < d:
            k += 1
        out.append(str(k))
    sys.stdout.write("\n".join(out) + "\n")


main()
