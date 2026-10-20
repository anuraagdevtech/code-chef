import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        total = sum(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        # Coins are conserved and the bags end up holding a multiple of k,
        # so the leftover is fixed regardless of where the split is made.
        out.append(str(total % k))
    sys.stdout.write("\n".join(out) + "\n")


main()
