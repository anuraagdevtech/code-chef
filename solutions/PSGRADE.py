import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        # Order: the three minimums, the total minimum, then the three scores.
        amin, bmin, cmin, tmin, a, b, c = map(int, data[1 + 7 * i:8 + 7 * i])
        ok = a >= amin and b >= bmin and c >= cmin and a + b + c >= tmin
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
