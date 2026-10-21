import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        w = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        peak = max(w)
        spots = [i for i, v in enumerate(w) if v == peak]
        half = n // 2
        # Each cyclic gap between consecutive maxima holds g - half + 1 windows.
        total = 0
        for j, p in enumerate(spots):
            nxt = spots[(j + 1) % len(spots)]
            gap = (nxt - p - 1) % n if len(spots) > 1 else n - 1
            total += max(0, gap - half + 1)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
