import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 4 * i]), int(data[2 + 4 * i])
        x, y = int(data[3 + 4 * i]), int(data[4 + 4 * i])
        # An adjacent vaccine claims the whole half-grid on its side.
        out.append(str(max(m * (n - x), m * (x - 1), n * (m - y), n * (y - 1))))
    sys.stdout.write("\n".join(out) + "\n")


main()
