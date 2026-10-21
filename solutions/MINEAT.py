import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, h = int(data[pos]), int(data[pos + 1])
        piles = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        # Hours needed is non-increasing in k, so binary search the threshold.
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            if sum((a + k - 1) // k for a in piles) <= h:
                hi = k
            else:
                lo = k + 1
        out.append(str(lo))
    sys.stdout.write("\n".join(out) + "\n")


main()
