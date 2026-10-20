import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, d = map(int, data[1 + 3 * i:4 + 3 * i])
        # Either team may be the stronger one, so compare the magnitude.
        out.append("YES" if abs(x - y) <= d else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
