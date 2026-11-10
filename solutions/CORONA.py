"""CodeChef CORONA — standalone Python 3 solution."""
import sys
from heapq import heapify,heappop,heappush



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,m,k = int(next(it)),int(next(it)),int(next(it))
        dist = [10**30]*n
        heap = []
        for _ in range(k):
            v,c = int(next(it))-1,int(next(it))
            dist[v] = c
            heap.append((c,v))
        heapify(heap)
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = int(next(it))-1,int(next(it))-1,int(next(it))
            adj[u].append((v,w))
            adj[v].append((u,w))
        while heap:
            cost,v = heappop(heap)
            if cost != dist[v]:
                continue
            for u,w in adj[v]:
                if cost+w < dist[u]:
                    dist[u] = cost+w
                    heappush(heap,(cost+w,u))
        out.append(' '.join(map(str,dist)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
