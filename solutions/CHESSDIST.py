import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x1, y1, x2, y2 = map(int, data[1 + 4 * i:5 + 4 * i])
        # King-move distance: the diagonal closes both gaps at once.
        out.append(str(max(abs(x1 - x2), abs(y1 - y2))))
    sys.stdout.write("\n".join(out) + "\n")


main()
