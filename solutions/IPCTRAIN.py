import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, d = int(data[pos]), int(data[pos + 1])
        pos += 2
        arriving = [[] for _ in range(d + 1)]
        total = 0
        for _ in range(n):
            day, want, sad = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
            pos += 3
            total += want * sad
            arriving[day].append([-sad, want])      # negated for a max-heap
        heap = []
        avoided = 0
        for day in range(1, d + 1):
            for trainer in arriving[day]:
                heapq.heappush(heap, trainer)
            if heap:
                top = heap[0]
                avoided -= top[0]
                # Only the quota changes, never the key, so the heap stays valid.
                top[1] -= 1
                if top[1] == 0:
                    heapq.heappop(heap)
        out.append(str(total - avoided))
    sys.stdout.write("\n".join(out) + "\n")


main()
