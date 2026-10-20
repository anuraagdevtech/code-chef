import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, m = map(int, data[1 + 3 * i:4 + 3 * i])
        d = abs(a - b)
        # Roads are bidirectional, so the two arcs sum to m.
        out.append(str(min(d, m - d)))
    sys.stdout.write("\n".join(out) + "\n")


main()
