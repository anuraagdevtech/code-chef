import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        a_first = (500 - 2 * x) + (1000 - 4 * (x + y))
        b_first = (1000 - 4 * y) + (500 - 2 * (x + y))
        # Whichever problem goes second pays the other's solving time.
        out.append(str(max(a_first, b_first)))
    sys.stdout.write("\n".join(out) + "\n")


main()
