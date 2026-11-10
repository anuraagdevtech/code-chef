"""CodeChef INSQ15_F — standalone Python 3 solution."""
import sys
from heapq import heappop,heappush



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    n,m = int(next(it)),int(next(it))
    h = [int(next(it)) for _ in range(n)]
    c = [int(next(it)) for _ in range(n)]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u,v = int(next(it))-1,int(next(it))-1
        adj[u].append(v)
        adj[v].append(u)
    dist = [[10**30,10**30] for _ in range(n)]
    dist[0] = [c[0],c[0]]
    heap = [(c[0],0,0),(c[0],0,1)]
    while heap:
        cost,v,mode = heappop(heap)
        if cost != dist[v][mode]:
            continue
        if cost+c[v] < dist[v][mode^1]:
            dist[v][mode^1] = cost+c[v]
            heappush(heap,(cost+c[v],v,mode^1))
        for u in adj[v]:
            if (mode == 0 and h[u] >= h[v]) or (mode == 1 and h[u] <= h[v]):
                if cost < dist[u][mode]:
                    dist[u][mode] = cost
                    heappush(heap,(cost,u,mode))
    answer = min(dist[-1])
    out.append(str(answer if answer < 10**30 else -1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
