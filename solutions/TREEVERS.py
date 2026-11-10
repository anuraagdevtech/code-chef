"""CodeChef TREEVERS — standalone Python 3 solution."""
import sys
from functools import cmp_to_key


def read_tree(it, n):
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = int(next(it))-1, int(next(it))-1
        adj[u].append(v)
        adj[v].append(u)
    return adj


def rooted(adj, root=0):
    parent = [-1]*len(adj)
    parent[root] = root
    order = [root]
    for v in order:
        for u in adj[v]:
            if parent[u] < 0:
                parent[u] = v
                order.append(u)
    return parent, order



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        w = [int(next(it)) for _ in range(n)]
        adj = read_tree(it,n)
        parent, order = rooted(adj)
        zeros, ones, inv = [0]*n,[0]*n,[0]*n
        for v in reversed(order):
            children = [u for u in adj[v] if parent[u] == v]
            children.sort(key=cmp_to_key(lambda a,b: (ones[a]*zeros[b] > ones[b]*zeros[a])-(ones[a]*zeros[b] < ones[b]*zeros[a])))
            zeros[v], ones[v] = 1-w[v],w[v]
            for u in children:
                inv[v] += inv[u]+ones[v]*zeros[u]
                zeros[v] += zeros[u]
                ones[v] += ones[u]
        out.append(str(inv[0]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
