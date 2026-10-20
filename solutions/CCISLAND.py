import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, xr, yr, d = map(int, data[1 + 5 * i:6 + 5 * i])
        # Food and water are not interchangeable, so both must hold.
        out.append("YES" if x >= xr * d and y >= yr * d else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
