import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 2                       # K itself is never needed
        rooms = defaultdict(list)
        for _ in range(n):
            s, f, p = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
            pos += 3
            rooms[p].append((f, s))
        served = 0
        for intervals in rooms.values():
            intervals.sort()           # by finishing time
            free_at = -1
            for f, s in intervals:
                # Intervals are half-open, so starting exactly at f is fine.
                if s >= free_at:
                    served += 1
                    free_at = f
        out.append(str(served))
    sys.stdout.write("\n".join(out) + "\n")


main()
