import sys
from collections import deque


def solve(tokens):
    n, k, anchor = (next(tokens), next(tokens), next(tokens) - 1)
    special = [next(tokens) - 1 for _ in range(k)]
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = (next(tokens) - 1, next(tokens) - 1)
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    order = [anchor]
    parent[anchor] = anchor
    for u in order:
        for v in graph[u]:
            if parent[v] < 0:
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)
    value = [-10 ** 9] * n
    witness = [-1] * n
    for u in special:
        value[u] = depth[u]
        witness[u] = u
    for u in reversed(order[1:]):
        up = parent[u]
        if value[u] - 1 > value[up]:
            value[up] = value[u] - 1
            witness[up] = witness[u]
    for u in order[1:]:
        up = parent[u]
        if value[up] - 1 > value[u]:
            value[u] = value[up] - 1
            witness[u] = witness[up]
    return ' '.join(map(str, value)) + '\n' + ' '.join((str(x + 1) for x in witness))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
