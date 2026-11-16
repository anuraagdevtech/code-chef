import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        edges = []
        for _ in range(m):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            if a[u] > a[v]:
                u,v = v,u
            if a[u] < a[v]:
                edges.append((a[v]-a[u],u,v))
        edges.sort()
        dp = [1]*n
        i = 0
        while i < len(edges):
            j = i
            pending = {}
            while j < len(edges) and edges[j][0] == edges[i][0]:
                _,u,v = edges[j]
                pending[v] = max(pending.get(v,1),dp[u]+1)
                j += 1
            for v,value in pending.items():
                dp[v] = max(dp[v],value)
            i = j
        out.append(str(max(dp)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
