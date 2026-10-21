import sys
from math import gcd

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, n = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        d = a - b
        if d == 0:
            out.append(str(2 * pow(a, n, MOD) % MOD))
            continue
        # A == B (mod d), so A^N + B^N collapses to 2 B^N there.
        out.append(str(gcd(2 * pow(b, n, d) % d, d) % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
