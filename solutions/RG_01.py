"""CodeChef RG_01 — standalone Python 3 solution."""
import sys


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
    n,m = int(next(it)),int(next(it))
    edges = []
    for _ in range(m):
        u,v,w = int(next(it)),int(next(it)),int(next(it))
        edges.append((w,u,v))
    d = DSU(n)
    adj = [[] for _ in range(n)]
    for w,u,v in sorted(edges,reverse=True):
        if d.union(u,v):
            adj[u].append((v,w))
            adj[v].append((u,w))
    for root in range(n):
        scores = [0]*n
        stack = [(root,-1,10**30)]
        while stack:
            v,p,score = stack.pop()
            if v != root:
                scores[v] = score
            for u,w in adj[v]:
                if u != p:
                    stack.append((u,v,min(score,w)))
        out.append(' '.join(map(str,scores)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
