import sys
from collections import deque


def solve(tokens):
    n, m, subjects, needed = (next(tokens), next(tokens), next(tokens), next(tokens))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = (next(tokens), next(tokens))
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1] * (n + 1)
    dist[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    costs = sorted((dist[next(tokens)] for _ in range(subjects)))
    return str(2 * sum(costs[:needed]))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
