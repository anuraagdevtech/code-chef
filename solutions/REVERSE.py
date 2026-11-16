import sys
from collections import deque


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = next(tokens)-1,next(tokens)-1
        graph[u].append((v,0))
        graph[v].append((u,1))
    distance = [n+m+1]*n
    distance[0] = 0
    queue = deque([(0,0)])
    while queue:
        current,u = queue.popleft()
        if current != distance[u]:
            continue
        for v,cost in graph[u]:
            candidate = current+cost
            if candidate < distance[v]:
                distance[v] = candidate
                if cost:
                    queue.append((candidate,v))
                else:
                    queue.appendleft((candidate,v))
    print(distance[-1] if distance[-1] < n+m+1 else -1)

if __name__ == '__main__':
    main()
