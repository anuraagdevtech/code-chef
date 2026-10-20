import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Weight of a position is how many triplets cover it: 1, 2, 3, ..., 2, 1.
        weight = [min(j, n - 2, n - j + 1, 3) for j in range(1, n + 1)]
        order = sorted(range(n), key=lambda j: weight[j])
        # Rearrangement inequality: largest values onto the lightest positions.
        perm = [0] * n
        for rank, idx in enumerate(order):
            perm[idx] = n - rank
        out.append(" ".join(map(str, perm)))
    sys.stdout.write("\n".join(out) + "\n")


main()
