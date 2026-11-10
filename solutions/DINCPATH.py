"""CodeChef DINCPATH — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, m = int(next(it)), int(next(it))
        a = [int(next(it)) for _ in range(n)]
        edges = []
        for _ in range(m):
            u, v = int(next(it))-1, int(next(it))-1
            if a[u] > a[v]:
                u,v = v,u
            if a[u] != a[v]:
                edges.append((a[v]-a[u],u,v))
        edges.sort()
        dp = [1]*n
        i = 0
        while i < len(edges):
            j = i
            updates = []
            while j < len(edges) and edges[j][0] == edges[i][0]:
                _,u,v = edges[j]
                updates.append((v,dp[u]+1))
                j += 1
            for v,value in updates:
                dp[v] = max(dp[v],value)
            i = j
        out.append(str(max(dp)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
