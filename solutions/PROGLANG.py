import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, a1, b1, a2, b2 = map(int, data[1 + 6 * i:7 + 6 * i])
        need = {a, b}
        # Features may be listed in either order, so compare as sets.
        if need <= {a1, b1}:
            out.append("1")
        elif need <= {a2, b2}:
            out.append("2")
        else:
            out.append("0")
    sys.stdout.write("\n".join(out) + "\n")


main()
