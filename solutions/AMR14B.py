"""CodeChef AMR14B — standalone Python 3 solution."""
import sys
from heapq import heappop,heappush


class DSU:
    def __init__(self, n):
        self.p = [-1]*n
        self.count = n

    def find(self, x):
        p = self.p
        while p[x] >= 0:
            if p[p[x]] >= 0:
                p[x] = p[p[x]]
            x = p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        p = self.p
        if p[a] > p[b]:
            a, b = b, a
        p[a] += p[b]
        p[b] = a
        self.count -= 1
        return True



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,m = int(next(it)),int(next(it))
        adj = [[] for _ in range(n)]
        edges = []
        for _ in range(m):
            u,v,w = int(next(it)),int(next(it)),int(next(it))
            adj[u].append((v,w))
            adj[v].append((u,w))
            edges.append((w,u,v))
        dist = [10**30]*n
        last = [10**30]*n
        dist[0] = last[0] = 0
        heap = [(0,0)]
        while heap:
            cost,v = heappop(heap)
            if cost != dist[v]:
                continue
            for u,w in adj[v]:
                nc = cost+w
                if nc < dist[u]:
                    dist[u],last[u] = nc,w
                    heappush(heap,(nc,u))
                elif nc == dist[u]:
                    last[u] = min(last[u],w)
        d = DSU(n)
        mst = 0
        for w,u,v in sorted(edges):
            if d.union(u,v):
                mst += w
        out.append('YES' if d.count == 1 and mst == sum(last) else 'NO')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
