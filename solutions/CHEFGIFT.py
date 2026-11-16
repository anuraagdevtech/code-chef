import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        budget,n,m = (int(next(tokens)) for _ in range(3))
        toll = [[int(next(tokens)) for _ in range(n)] for _ in range(m)]
        cost = [[int(next(tokens)) for _ in range(m)] for _ in range(m)]
        for k in range(m):
            for i in range(m):
                via = cost[i][k]
                for j in range(m):
                    cost[i][j] = min(cost[i][j],via+cost[k][j])
        dp = [row[0] for row in toll]
        for stage in range(1,n):
            dp = [toll[j][stage]+min(dp[i]+cost[i][j] for i in range(m)) for j in range(m)]
        remaining = budget-min(dp)
        out.append(str(remaining if remaining >= 0 else -1))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
