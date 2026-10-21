import sys
from collections import Counter

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    counts = Counter(data[2:2 + n]).values()
    m = len(counts)
    # Only m distinct values exist, so no good subsequence is longer than m.
    k = min(k, m)
    dp = [0] * (k + 1)
    dp[0] = 1
    for c in counts:
        # Downward so each value contributes to at most one chosen slot.
        for j in range(min(k, m), 0, -1):
            dp[j] = (dp[j] + c * dp[j - 1]) % MOD
    sys.stdout.write(f"{sum(dp) % MOD}\n")


main()
