"""CodeChef CHEFGIFT — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        budget,n,m = int(next(it)),int(next(it)),int(next(it))
        toll = [[int(next(it)) for _ in range(n)] for _ in range(m)]
        cost = [[int(next(it)) for _ in range(m)] for _ in range(m)]
        for k in range(m):
            for i in range(m):
                ik = cost[i][k]
                for j in range(m):
                    cost[i][j] = min(cost[i][j],ik+cost[k][j])
        dp = [toll[i][0] for i in range(m)]
        for pos in range(1,n):
            dp = [toll[j][pos]+min(dp[i]+cost[i][j] for i in range(m)) for j in range(m)]
        remaining = budget-min(dp)
        out.append(str(remaining if remaining >= 0 else -1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
