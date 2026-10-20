import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Lower time wins; the tie needs its own branch.
        out.append("BIKE" if x < y else "CAR" if y < x else "SAME")
    sys.stdout.write("\n".join(out) + "\n")


main()
