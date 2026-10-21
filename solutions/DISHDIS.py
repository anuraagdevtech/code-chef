import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        pos += 2
        ranges = [(int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])) for i in range(m)]
        pos += 2 * m
        dp = [0] * (n + 1)
        dp[0] = 1
        for lo, hi in ranges:
            if lo > hi:                 # an empty range admits nothing
                dp = [0] * (n + 1)
                break
            pref = [0] * (n + 2)
            for j in range(n + 1):
                pref[j + 1] = (pref[j] + dp[j]) % MOD
            nxt = [0] * (n + 1)
            for j in range(n + 1):
                # Window [j - hi, j - lo] of the previous row.
                top = j - lo
                if top < 0:
                    continue
                bottom = j - hi
                if bottom < 0:
                    bottom = 0
                nxt[j] = (pref[top + 1] - pref[bottom]) % MOD
            dp = nxt
        out.append(str(dp[n] % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
