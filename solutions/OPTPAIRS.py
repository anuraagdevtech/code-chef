import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # Every divisor d < N/2 gives the pair (d, N - d) in two orders.
        small = 0
        for d in range(1, isqrt(n) + 1):
            if n % d:
                continue
            if 2 * d < n:
                small += 1
            other = n // d
            if other != d and 2 * other < n:
                small += 1
        out.append(str(2 * small + (n % 2 == 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
