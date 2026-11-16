import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m,price = (int(next(tokens)) for _ in range(3))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v = int(next(tokens)),int(next(tokens))
            graph[u].append(v)
            graph[v].append(u)
        tin = [-1]*n
        low = [0]*n
        parent = [-1]*n
        children = [0]*n
        cut = [False]*n
        timer = 0
        for start in range(n):
            if tin[start] != -1:
                continue
            tin[start] = low[start] = timer
            timer += 1
            stack = [(start,0)]
            while stack:
                u,index = stack[-1]
                if index == len(graph[u]):
                    stack.pop()
                    p = parent[u]
                    if p == -1:
                        cut[u] = children[u] > 1
                    else:
                        low[p] = min(low[p],low[u])
                        if parent[p] != -1 and low[u] >= tin[p]:
                            cut[p] = True
                    continue
                v = graph[u][index]
                stack[-1] = (u,index+1)
                if v == parent[u]:
                    continue
                if tin[v] != -1:
                    low[u] = min(low[u],tin[v])
                else:
                    parent[v] = u
                    children[u] += 1
                    tin[v] = low[v] = timer
                    timer += 1
                    stack.append((v,0))
        out.append(str(sum(cut)*price))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
