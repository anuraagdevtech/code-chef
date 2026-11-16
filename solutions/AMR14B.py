import sys
from heapq import heappush,heappop


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = (int(next(tokens)) for _ in range(3))
            graph[u].append((v,w))
            graph[v].append((u,w))
        infinity = 10**30
        distance = [infinity]*n
        last = [infinity]*n
        distance[0] = last[0] = 0
        heap = [(0,0)]
        while heap:
            d,u = heappop(heap)
            if d != distance[u]:
                continue
            for v,w in graph[u]:
                candidate = d+w
                if candidate < distance[v]:
                    distance[v],last[v] = candidate,w
                    heappush(heap,(candidate,v))
                elif candidate == distance[v]:
                    last[v] = min(last[v],w)
        if any(d == infinity for d in distance):
            out.append('NO')
            continue
        seen = [False]*n
        heap = [(0,0)]
        mst = 0
        while heap:
            weight,u = heappop(heap)
            if seen[u]:
                continue
            seen[u] = True
            mst += weight
            for v,w in graph[u]:
                if not seen[v]:
                    heappush(heap,(w,v))
        out.append('YES' if sum(last) == mst else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
