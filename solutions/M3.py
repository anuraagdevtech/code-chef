"""League elimination via redistribution of remaining match wins."""
import sys
from collections import deque


def feasible(n, matches, wins, candidate, limit):
    if max(wins) > limit:
        return False
    source, sink = n, n+1
    graph = [[] for _ in range(n+2)]

    def add(u,v,capacity):
        graph[u].append([v,len(graph[v]),capacity])
        graph[v].append([u,len(graph[u])-1,0])

    baseline = wins[:]
    for u,v in matches:
        if u == candidate or v == candidate:
            continue
        baseline[u] += 1
        add(u,v,1)
    required = 0
    for v in range(n):
        if v == candidate:
            continue
        excess = baseline[v]-limit
        if excess > 0:
            add(source,v,excess)
            required += excess
        elif excess < 0:
            add(v,sink,-excess)
    flow = 0
    while flow < required:
        level = [-1]*(n+2)
        level[source] = 0
        queue = deque([source])
        while queue:
            v = queue.popleft()
            for u,_,cap in graph[v]:
                if cap and level[u] < 0:
                    level[u] = level[v]+1
                    queue.append(u)
        if level[sink] < 0:
            return False
        ptr = [0]*(n+2)

        def send(v,amount):
            if v == sink:
                return amount
            while ptr[v] < len(graph[v]):
                edge = graph[v][ptr[v]]
                u,reverse,cap = edge
                if cap and level[u] == level[v]+1:
                    sent = send(u,min(amount,cap))
                    if sent:
                        edge[2] -= sent
                        graph[u][reverse][2] += sent
                        return sent
                ptr[v] += 1
            return 0

        while flow < required:
            sent = send(source,required-flow)
            if not sent:
                break
            flow += sent
    return True


def solve():
    it = iter(map(int,sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(it)):
        n = next(it)
        matrix = [[next(it) for _ in range(n)] for _ in range(n)]
        wins = [row.count(1) for row in matrix]
        remaining = [row.count(2) for row in matrix]
        matches = [(u,v) for u in range(n) for v in range(u+1,n) if matrix[u][v] == 2]
        answer = []
        for candidate in range(n):
            limit = wins[candidate]+remaining[candidate]
            answer.append('1' if feasible(n,matches,wins,candidate,limit) else '0')
        out.append(''.join(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    solve()
