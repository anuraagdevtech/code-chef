import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, a, b = map(int, data[1 + 4 * i:5 + 4 * i])
        # Gold in Chef's races that the rival did not enter.
        out.append(str(len({x, y} - {a, b})))
    sys.stdout.write("\n".join(out) + "\n")


main()
