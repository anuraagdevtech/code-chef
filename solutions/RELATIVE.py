import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        g, c = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # v^2 = 2gH with v = c; 2g is guaranteed to divide c^2 exactly.
        out.append(str(c * c // (2 * g)))
    sys.stdout.write("\n".join(out) + "\n")


main()
