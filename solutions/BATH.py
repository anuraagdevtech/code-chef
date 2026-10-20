import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # One bath costs exactly 2 * y litres; leftover water is wasted.
        out.append(str(x // (2 * y)))
    sys.stdout.write("\n".join(out) + "\n")


main()
