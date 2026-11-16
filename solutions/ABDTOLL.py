import sys
from heapq import heappush,heappop


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,root,budget = (int(next(tokens)) for _ in range(3))
        root -= 1
        toll = [int(next(tokens)) for _ in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        active = [False]*n
        heap = []
        path_sum = reductions = 0
        stack = [(root,-1,0,False)]
        while stack:
            u,parent,depth,exit_event = stack.pop()
            if exit_event:
                path_sum -= toll[u]
                active[u] = False
                continue
            active[u] = True
            path_sum += toll[u]
            heappush(heap,(depth,u))
            while path_sum > budget:
                while heap and (not active[heap[0][1]] or toll[heap[0][1]] == 0):
                    heappop(heap)
                v = heap[0][1]
                reduction = min(toll[v],path_sum-budget)
                toll[v] -= reduction
                reductions += reduction
                path_sum -= reduction
            stack.append((u,parent,depth,True))
            for v in graph[u]:
                if v != parent:
                    stack.append((v,u,depth+1,False))
        out.append(str(2*reductions))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
