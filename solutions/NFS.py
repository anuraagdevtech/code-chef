import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        u, v, a, s = map(int, data[1 + 4 * i:5 + 4 * i])
        # Compare squares: no sqrt, and a negative left side (the car stops
        # before the turn) is handled without a special case.
        out.append("Yes" if u * u - 2 * a * s <= v * v else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
