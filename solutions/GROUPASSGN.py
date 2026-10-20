import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Every pair sums to 2n + 1, so the partner is the reflection of x.
        out.append(str(2 * n + 1 - x))
    sys.stdout.write("\n".join(out) + "\n")


main()
