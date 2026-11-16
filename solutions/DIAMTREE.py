import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        def farthest(start):
            distance = [-1]*n
            distance[start] = 0
            queue = deque([start])
            last = start
            while queue:
                last = queue.popleft()
                for v in graph[last]:
                    if distance[v] == -1:
                        distance[v] = distance[last]+1
                        queue.append(v)
            return last,distance[last]
        endpoint,_ = farthest(0)
        _,diameter = farthest(endpoint)
        out.append(str(diameter))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
