"""CodeChef DIAMTREE — standalone Python 3 solution."""
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
        end = 0
        for _ in range(2):
            dist = [-1]*n
            dist[end] = 0
            order = [end]
            for v in order:
                for u in adj[v]:
                    if dist[u] < 0:
                        dist[u] = dist[v]+1
                        order.append(u)
            end = max(range(n), key=dist.__getitem__)
        out.append(str(dist[end]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
