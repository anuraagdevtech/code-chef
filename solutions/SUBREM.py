import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,x = int(next(tokens)),int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
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
        dp = a[:]
        for u in reversed(order):
            dp[u] = max(-x,dp[u])
            if parent[u] != -1:
                dp[parent[u]] += dp[u]
        out.append(str(dp[0]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
