import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        angles = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # 360 must be in the gcd so the pattern closes up over a full turn.
        d = 360
        base = angles[0]
        for a in angles[1:]:
            d = gcd(d, a - base)
        out.append(str(360 // d - n))
    sys.stdout.write("\n".join(out) + "\n")


main()
