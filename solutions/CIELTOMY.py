"""CodeChef CIELTOMY — standalone Python 3 solution."""
import sys
from heapq import heappop,heappush



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,m = int(next(it)),int(next(it))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = int(next(it))-1,int(next(it))-1,int(next(it))
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist,ways = [10**30]*n,[0]*n
        dist[0],ways[0] = 0,1
        heap = [(0,0)]
        while heap:
            cost,v = heappop(heap)
            if cost != dist[v]:
                continue
            for u,w in adj[v]:
                nc = cost+w
                if nc < dist[u]:
                    dist[u],ways[u] = nc,ways[v]
                    heappush(heap,(nc,u))
                elif nc == dist[u]:
                    ways[u] += ways[v]
        out.append(str(ways[-1]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
