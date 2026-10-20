import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        l, r = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Sums sweep [2L, 2R] with no gaps, since unit steps are available.
        out.append(str(2 * r - 2 * l + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
