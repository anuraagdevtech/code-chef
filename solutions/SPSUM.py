import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        s = n * (n + 1) // 2
        # The two sums are forced; any target in [0, s] is a reachable subset sum.
        if m > s or (s + m) % 2:
            out.append("No")
            continue
        a, b = (s + m) // 2, (s - m) // 2
        out.append("Yes" if gcd(a, b) == 1 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
