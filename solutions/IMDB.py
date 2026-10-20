import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        pos += 2
        best = 0
        for i in range(n):
            s, r = int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])
            # Only movies that fit are candidates; exactly X GB still fits.
            if s <= x and r > best:
                best = r
        pos += 2 * n
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
