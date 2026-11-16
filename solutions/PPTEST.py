import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,budget = int(next(tokens)),int(next(tokens))
        dp = [0]*(budget+1)
        for _ in range(n):
            count,points,time = (int(next(tokens)) for _ in range(3))
            value = count*points
            for capacity in range(budget,time-1,-1):
                dp[capacity] = max(dp[capacity],dp[capacity-time]+value)
        out.append(str(dp[budget]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
