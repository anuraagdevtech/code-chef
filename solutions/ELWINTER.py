import sys
import sys, heapq


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    m = next(tokens)
    q = next(tokens)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(tokens) - 1
        v = next(tokens) - 1
        graph[u].append(v)
        graph[v].append(u)
    frozen = [False] * n
    events = []
    now = 0
    out = []
    for _ in range(q):
        kind = next(tokens)
        x = next(tokens)
        if kind == 1:
            if not frozen[x - 1]:
                frozen[x - 1] = True
                heapq.heappush(events, (now, x - 1))
        elif kind == 2:
            now += x
            while events and events[0][0] < now:
                t, u = heapq.heappop(events)
                for v in graph[u]:
                    if not frozen[v]:
                        frozen[v] = True
                        heapq.heappush(events, (t + 1, v))
        else:
            out.append('YES' if frozen[x - 1] else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
