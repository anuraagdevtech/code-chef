"""CodeChef TR1 — standalone Python 3 solution."""
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
        parent,order = rooted(adj)
        size = [1]*n
        answer = 0
        for v in reversed(order):
            squares = 0
            for u in adj[v]:
                if parent[u] == v:
                    size[v] += size[u]
                    squares += size[u]*size[u]
            count = size[v]*size[v]-squares
            answer = (answer+(v+1)*count) % 1000000007
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
