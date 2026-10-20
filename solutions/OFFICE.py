import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Mon-Thu is four days at x hours, Friday is y, weekend is zero.
        out.append(str(4 * x + y))
    sys.stdout.write("\n".join(out) + "\n")


main()
