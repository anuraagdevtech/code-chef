"""CodeChef DIGJUMP — standalone Python 3 solution."""
import sys
from collections import deque



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    s = next(it)
    n = len(s)
    positions = [[] for _ in range(10)]
    for i,c in enumerate(s):
        positions[c-48].append(i)
    dist = [-1]*n
    dist[0] = 0
    queue = deque([0])
    while queue:
        v = queue.popleft()
        if v == n-1:
            break
        digit = s[v]-48
        neighbors = positions[digit]
        positions[digit] = []
        if v:
            neighbors.append(v-1)
        if v+1 < n:
            neighbors.append(v+1)
        for u in neighbors:
            if dist[u] < 0:
                dist[u] = dist[v]+1
                queue.append(u)
    out.append(str(dist[-1]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
