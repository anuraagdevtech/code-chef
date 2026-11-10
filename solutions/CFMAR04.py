"""CodeChef CFMAR04 — standalone Python 3 solution."""
import sys
from collections import Counter



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    n = int(next(it))
    groups = Counter()
    for _ in range(n):
        counts = [0]*26
        for c in next(it):
            counts[c-97] += 1
        groups[tuple(counts)] += 1
    out.append(str(max(groups.values())))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
