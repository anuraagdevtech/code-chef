import sys
import heapq


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        m = next(tokens)
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u = next(tokens) - 1
            v = next(tokens) - 1
            graph[u].append(v)
            graph[v].append(u)
        dist = [n + 1] * n
        dist[0] = 0
        from collections import deque
        queue = deque([0])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] > dist[u]:
                    dist[v] = dist[u]
                    queue.appendleft(v)
            for v in (u - 1, u + 1):
                if 0 <= v < n and dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        out.append(str(dist[-1]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
