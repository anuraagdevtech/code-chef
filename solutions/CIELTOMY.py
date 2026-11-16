import sys
from heapq import heappush,heappop


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = int(next(tokens))-1,int(next(tokens))-1,int(next(tokens))
            graph[u].append((v,w))
            graph[v].append((u,w))
        distance = [10**30]*n
        ways = [0]*n
        distance[0] = 0
        ways[0] = 1
        heap = [(0,0)]
        while heap:
            d,u = heappop(heap)
            if d != distance[u]:
                continue
            for v,w in graph[u]:
                candidate = d+w
                if candidate < distance[v]:
                    distance[v] = candidate
                    ways[v] = ways[u]
                    heappush(heap,(candidate,v))
                elif candidate == distance[v]:
                    ways[v] += ways[u]
        out.append(str(ways[-1]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
