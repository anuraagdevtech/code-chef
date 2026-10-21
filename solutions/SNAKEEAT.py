import sys
from bisect import bisect_left


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, q = int(data[pos]), int(data[pos + 1])
        lengths = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        prefix = [0] * (n + 1)
        for i, v in enumerate(lengths):
            prefix[i + 1] = prefix[i] + v
        for i in range(q):
            k = int(data[pos + i])
            # First index already long enough; everything before it is short.
            short_end = bisect_left(lengths, k)

            def feasible(m):
                lo = n - m
                hi = min(short_end, n)          # kept snakes below k
                if lo >= hi:
                    return True
                need = k * (hi - lo) - (prefix[hi] - prefix[lo])
                return need <= n - m

            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if feasible(mid):
                    lo = mid
                else:
                    hi = mid - 1
            out.append(str(lo))
        pos += q
    sys.stdout.write("\n".join(out) + "\n")


main()
