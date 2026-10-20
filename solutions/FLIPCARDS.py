import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Flip the up ones, or the down ones, whichever is cheaper.
        out.append(str(min(x, n - x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
