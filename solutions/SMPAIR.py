import sys
import heapq


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Two distinct positions, so equal values are still a valid pair.
        lo1, lo2 = heapq.nsmallest(2, a)
        out.append(str(lo1 + lo2))
    sys.stdout.write("\n".join(out) + "\n")


main()
