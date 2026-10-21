import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        spots = [[] for _ in range(n + 1)]
        for i in range(n):
            spots[int(data[pos + 1 + i])].append(i + 1)
        pos += 1 + n
        total = 0
        for length in range(1, n + 1):
            last = 0          # rightmost left-end already counted
            for p in spots[length]:
                lo = max(1, p - length + 1, last + 1)
                hi = min(p, n - length + 1)
                if hi >= lo:
                    total += hi - lo + 1
                    last = hi
            # Intervals arrive sorted, so "last" merges the overlaps in place.
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
