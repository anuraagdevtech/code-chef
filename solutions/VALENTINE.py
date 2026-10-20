import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Change left over buys nothing, so round down.
        out.append(str(x // y))
    sys.stdout.write("\n".join(out) + "\n")


main()
