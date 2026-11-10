"""CodeChef COSTEMP — standalone Python 3 solution."""
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
    n = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = int(next(it)), int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    parent, order = rooted(adj)
    size = [1]*n
    down = [0]*n
    for v in reversed(order[1:]):
        p = parent[v]
        size[p] += size[v]
        down[p] += down[v]+size[v]
    answer = [0]*n
    answer[0] = down[0]
    for v in order[1:]:
        answer[v] = answer[parent[v]]+n-2*size[v]
    out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
