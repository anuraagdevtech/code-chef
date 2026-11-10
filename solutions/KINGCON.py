"""CodeChef KINGCON — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,m,k = int(next(it)),int(next(it)),int(next(it))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u,v = int(next(it)),int(next(it))
            adj[u].append(v)
            adj[v].append(u)
        tin,low,parent,child = [-1]*n,[0]*n,[-1]*n,[0]*n
        cut = bytearray(n)
        timer = 0
        for root in range(n):
            if tin[root] >= 0:
                continue
            tin[root] = low[root] = timer
            timer += 1
            stack = [(root,iter(adj[root]))]
            while stack:
                v,neighbors = stack[-1]
                u = next(neighbors,None)
                if u is None:
                    stack.pop()
                    p = parent[v]
                    if p >= 0:
                        low[p] = min(low[p],low[v])
                        if parent[p] >= 0 and low[v] >= tin[p]:
                            cut[p] = 1
                    elif child[v] > 1:
                        cut[v] = 1
                elif u != parent[v]:
                    if tin[u] < 0:
                        parent[u] = v
                        child[v] += 1
                        tin[u] = low[u] = timer
                        timer += 1
                        stack.append((u,iter(adj[u])))
                    else:
                        low[v] = min(low[v],tin[u])
        out.append(str(sum(cut)*k))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
