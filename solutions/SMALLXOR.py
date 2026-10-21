import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x, y = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        heap = [int(v) for v in data[pos + 3:pos + 3 + n]]
        pos += 3 + n
        heapq.heapify(heap)
        for step in range(y):
            v = heap[0]
            flipped = v ^ x
            if flipped > v:
                heapq.heapreplace(heap, flipped)      # low form, so promote
            else:
                # High form: it stays the minimum and just toggles from here.
                left = y - step
                heapq.heapreplace(heap, flipped if left % 2 else v)
                break
        out.append(" ".join(map(str, sorted(heap))))
    sys.stdout.write("\n".join(out) + "\n")


main()
