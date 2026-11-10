"""CodeChef FIRE — standalone Python 3 solution."""
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
        n,source,t = int(next(it)),int(next(it))-1,int(next(it))
        adj = []
        for _ in range(n):
            count = int(next(it))
            adj.append([int(next(it))-1 for _ in range(count)])
        targets = {int(next(it))-1 for _ in range(t)}
        parent,order = rooted(adj,source)
        contains = [False]*n
        possible = [True]*n
        for v in reversed(order):
            relevant = [u for u in adj[v] if parent[u] == v and u != v and contains[u]]
            contains[v] = v in targets or bool(relevant)
            possible[v] = v not in targets and (len(relevant) < 2 or any(possible[u] for u in relevant))
        out.append('yes' if possible[source] else 'no')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
