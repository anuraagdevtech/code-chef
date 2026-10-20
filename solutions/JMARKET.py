import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, a, b, c = map(int, data[1 + 4 * i:5 + 4 * i])
        lo, mid, _ = sorted((a, b, c))
        # Exactly one unit must be a second kind; make it the cheapest such.
        out.append(str((x - 1) * lo + mid))
    sys.stdout.write("\n".join(out) + "\n")


main()
