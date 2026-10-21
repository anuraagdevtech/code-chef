import sys
from bisect import bisect_left


def main() -> None:
    # Numbers with exactly two set bits; 32 bits is past the 10^9 bound.
    targets = sorted((1 << x) + (1 << y) for y in range(32) for x in range(y))
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        i = bisect_left(targets, n)
        best = targets[i] - n
        if i:                                 # the lower neighbour may be nearer
            best = min(best, n - targets[i - 1])
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
