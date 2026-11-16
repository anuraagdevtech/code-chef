import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            u = next(tokens) - 1
            v = next(tokens) - 1
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        order = [0]
        parent[0] = 0
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        subtree_gcd = values[:]
        child_gcd_sum = [0] * n
        for u in reversed(order[1:]):
            up = parent[u]
            subtree_gcd[up] = gcd(subtree_gcd[up], subtree_gcd[u])
            child_gcd_sum[up] += subtree_gcd[u]
        best = [0] * n
        for u in reversed(order):
            best[u] = child_gcd_sum[u] + max([0] + [best[v] - subtree_gcd[v] for v in graph[u] if parent[v] == u])
        out.append(str(best[0]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
