import sys
from heapq import heappush,heappop


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m,k = (int(next(tokens)) for _ in range(3))
        distance = [10**30]*n
        heap = []
        for _ in range(k):
            city,price = int(next(tokens))-1,int(next(tokens))
            distance[city] = price
            heappush(heap,(price,city))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = int(next(tokens))-1,int(next(tokens))-1,int(next(tokens))
            graph[u].append((v,w))
            graph[v].append((u,w))
        while heap:
            d,u = heappop(heap)
            if d != distance[u]:
                continue
            for v,w in graph[u]:
                candidate = d+w
                if candidate < distance[v]:
                    distance[v] = candidate
                    heappush(heap,(candidate,v))
        out.append(' '.join(map(str,distance)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
