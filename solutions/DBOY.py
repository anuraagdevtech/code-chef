import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        h = [int(next(tokens)) for _ in range(n)]
        coins = set(int(next(tokens)) for _ in range(n))
        limit = 2*max(h)
        dp = [limit+1]*(limit+1)
        dp[0] = 0
        for coin in coins:
            for total in range(coin,limit+1):
                dp[total] = min(dp[total],dp[total-coin]+1)
        out.append(str(sum(dp[2*v] for v in h)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
