import sys
from bisect import bisect_right


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        pos += 2
        intervals = sorted((int(data[pos + 2 * i]), int(data[pos + 2 * i + 1]))
                           for i in range(n))
        pos += 2 * n
        starts = [l for l, _ in intervals]
        for i in range(m):
            p = int(data[pos + i])
            k = bisect_right(starts, p)
            # Intervals are half-open, so arriving exactly at R means waiting.
            if k and p < intervals[k - 1][1]:
                out.append("0")
            elif k < n:
                out.append(str(starts[k] - p))
            else:
                out.append("-1")
        pos += m
    sys.stdout.write("\n".join(out) + "\n")


main()
