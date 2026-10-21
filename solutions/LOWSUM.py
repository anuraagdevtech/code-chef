import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        k, q = int(data[pos]), int(data[pos + 1])
        pos += 2
        a = sorted(int(x) for x in data[pos:pos + k])
        pos += k
        b = sorted(int(x) for x in data[pos:pos + k])
        pos += k
        queries = [int(x) for x in data[pos:pos + q]]
        pos += q
        need = max(queries)
        # Rank <= need can never use anything past the need-th smallest value.
        m = min(k, need)
        a = a[:m]
        b = b[:m]
        # One head per row: the grid is m lists already sorted along j.
        heap = [(a[i] + b[0], i, 0) for i in range(m)]
        heapq.heapify(heap)
        sums = []
        while heap and len(sums) < need:
            total, i, j = heapq.heappop(heap)
            sums.append(total)
            if j + 1 < m:
                heapq.heappush(heap, (a[i] + b[j + 1], i, j + 1))
        out.extend(str(sums[v - 1]) for v in queries)
    sys.stdout.write("\n".join(out) + "\n")


main()
