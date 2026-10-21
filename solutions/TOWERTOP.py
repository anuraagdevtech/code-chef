import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Doubling reaches 2^(k-1) after k operations; afterwards the inventory
        # stays at or above X, so each further operation is a whole tower.
        k = (x - 1).bit_length() + 1
        out.append(str(max(0, m - k + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
