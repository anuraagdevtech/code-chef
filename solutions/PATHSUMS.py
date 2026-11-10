"""CodeChef PATHSUMS — standalone Python 3 solution."""
import sys


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
        adj = read_tree(it,n)
        parent, order = rooted(adj)
        labels = [1]*n
        for v in order[1:]:
            labels[v] = 3-labels[parent[v]]
        out.append(' '.join(map(str,labels)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
