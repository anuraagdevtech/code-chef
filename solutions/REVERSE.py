"""CodeChef REVERSE — standalone Python 3 solution."""
import sys
from collections import deque



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    n, m = int(next(it)), int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = int(next(it))-1, int(next(it))-1
        adj[u].append((v,0))
        adj[v].append((u,1))
    dist = [n+1]*n
    dist[0] = 0
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for u,w in adj[v]:
            if dist[v]+w < dist[u]:
                dist[u] = dist[v]+w
                if w:
                    queue.append(u)
                else:
                    queue.appendleft(u)
    out.append(str(dist[-1] if dist[-1] <= n else -1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
