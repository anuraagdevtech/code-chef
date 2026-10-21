import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[1 + i])
        # Shifting the cyclic square by (k+1)/2 pushes the diagonal of 1s
        # as far from the centre as a Latin square allows.
        s = (k + 1) // 2
        for r in range(k):
            row = [str((c - r - s) % k + 1) for c in range(k)]
            out.append(" ".join(row))
    sys.stdout.write("\n".join(out) + "\n")


main()
