import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x1, x2, y1, y2 = map(int, data[1 + 4 * i:5 + 4 * i])
        # Cost per km is y/x; cross-multiply to keep it exact.
        car1, car2 = y1 * x2, y2 * x1
        out.append("-1" if car1 < car2 else "1" if car2 < car1 else "0")
    sys.stdout.write("\n".join(out) + "\n")


main()
