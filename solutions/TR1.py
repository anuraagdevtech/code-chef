import sys


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
        parent = [-1]*n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        size = [1]*n
        child_squares = [0]*n
        answer = 0
        for u in reversed(order):
            answer += (u+1)*(size[u]*size[u]-child_squares[u])
            if parent[u] != -1:
                size[parent[u]] += size[u]
                child_squares[parent[u]] += size[u]*size[u]
        out.append(str(answer%1000000007))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
