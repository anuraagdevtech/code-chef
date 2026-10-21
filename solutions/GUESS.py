import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # An odd sum needs one odd and one even pick.
        top = (n + 1) // 2 * (m // 2) + n // 2 * ((m + 1) // 2)
        bottom = n * m
        g = gcd(top, bottom)          # gcd(0, d) == d, so 0 reduces to 0/1
        out.append(f"{top // g}/{bottom // g}")
    sys.stdout.write("\n".join(out) + "\n")


main()
