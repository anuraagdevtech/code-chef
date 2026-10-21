import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, a, b, k = (int(data[1 + 4 * i]), int(data[2 + 4 * i]),
                      int(data[3 + 4 * i]), int(data[4 + 4 * i]))
        lcm = a // gcd(a, b) * b
        # Common multiples are barred from both shares, hence subtracted twice.
        solved = n // a + n // b - 2 * (n // lcm)
        out.append("Win" if solved >= k else "Lose")
    sys.stdout.write("\n".join(out) + "\n")


main()
