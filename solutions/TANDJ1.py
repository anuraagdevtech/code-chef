import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d, k = map(int, data[1 + 5 * i:6 + 5 * i])
        dist = abs(a - c) + abs(b - d)
        # Surplus steps must be wasted in pairs, so the gap must be even.
        out.append("YES" if k >= dist and (k - dist) % 2 == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
