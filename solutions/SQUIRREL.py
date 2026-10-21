import sys
import heapq


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        m, n, k = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        times = [int(v) for v in data[pos + 3:pos + 3 + m]]
        periods = [int(v) for v in data[pos + 3 + m:pos + 3 + 2 * m]]
        pos += 3 + 2 * m

        def harvest(s):
            counts = [(s - ti) // pi + 1 for ti, pi in zip(times, periods) if s >= ti]
            # Squirrels occupy n different trees, so take the n best.
            return sum(heapq.nlargest(n, counts)) if counts else 0

        lo, hi = 0, 10 ** 9 + 200
        while lo < hi:
            mid = (lo + hi) // 2
            if harvest(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        out.append(str(lo))
    sys.stdout.write("\n".join(out) + "\n")


main()
