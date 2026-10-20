import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p, m, v = map(int, data[1 + 3 * i:4 + 3 * i])
        # The driver is already priced into m, so only p - 1 extras cost.
        out.append(str(v * (m - p + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
