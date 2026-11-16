import sys
from heapq import heappush,heappop


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    height = [next(tokens) for _ in range(n)]
    cost = [next(tokens) for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = next(tokens)-1,next(tokens)-1
        graph[u].append(v)
        graph[v].append(u)
    infinity = 10**30
    distance = [infinity]*(2*n)
    distance[0] = distance[1] = cost[0]
    heap = [(cost[0],0),(cost[0],1)]
    while heap:
        d,state = heappop(heap)
        if d != distance[state]:
            continue
        u,mode = divmod(state,2)
        switched = state^1
        if d+cost[u] < distance[switched]:
            distance[switched] = d+cost[u]
            heappush(heap,(distance[switched],switched))
        for v in graph[u]:
            if (mode == 0 and height[v] >= height[u]) or (mode == 1 and height[v] <= height[u]):
                target = 2*v+mode
                if d < distance[target]:
                    distance[target] = d
                    heappush(heap,(d,target))
    answer = min(distance[-2:])
    print(answer if answer < infinity else -1)

if __name__ == '__main__':
    main()
