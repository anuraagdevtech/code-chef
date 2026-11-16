import sys
from collections import defaultdict
from heapq import heappush, heappop


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        groups = defaultdict(list)
        for _ in range(n):
            left,right,speed = (int(next(tokens)) for _ in range(3))
            groups[speed].append((left,right))
        possible = True
        for intervals in groups.values():
            active = []
            for left,right in sorted(intervals):
                while active and active[0] < left:
                    heappop(active)
                if len(active) >= 2:
                    possible = False
                    break
                heappush(active,right)
            if not possible:
                break
        out.append('YES' if possible else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
