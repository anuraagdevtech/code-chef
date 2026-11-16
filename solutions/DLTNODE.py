import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        graph = [[] for _ in range(n)]
        for _ in range(n - 1):
            u = next(tokens) - 1
            v = next(tokens) - 1
            graph[u].append(v)
            graph[v].append(u)
        values = [next(tokens) for _ in range(n)]
        parent = [-1] * n
        order = [0]
        parent[0] = 0
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        subtree_gcd = values[:]
        outside_gcd = [0] * n
        for u in reversed(order[1:]):
            subtree_gcd[parent[u]] = gcd(subtree_gcd[parent[u]], subtree_gcd[u])
        best = 0
        for u in order:
            children = [v for v in graph[u] if parent[v] == u]
            best = max(best, outside_gcd[u] + sum((subtree_gcd[v] for v in children)))
            prefix = [gcd(outside_gcd[u], values[u])]
            for v in children:
                prefix.append(gcd(prefix[-1], subtree_gcd[v]))
            suffix = 0
            for i in range(len(children) - 1, -1, -1):
                v = children[i]
                outside_gcd[v] = gcd(prefix[i], suffix)
                suffix = gcd(suffix, subtree_gcd[v])
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
