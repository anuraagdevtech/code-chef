import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m, k = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        g = gcd(k, m)
        if n % g:
            out.append("-1")              # tK can never hit N modulo M
            continue
        mod = m // g
        throws = (n // g) * pow(k // g, -1, mod) % mod if mod > 1 else 0
        # He cannot throw away more candies than he has.
        out.append(str(throws) if throws * k <= n else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
