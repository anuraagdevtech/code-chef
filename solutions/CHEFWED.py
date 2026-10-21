import sys

FAMILIES = 101


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        fam = [int(x) for x in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        dp = [0] + [None] * n
        for i in range(n):
            base = dp[i]
            seen = [0] * FAMILIES
            cost = 0
            for j in range(i, n):
                seen[fam[j]] += 1
                c = seen[fam[j]]
                # The second member makes *two* guests arguers at once.
                if c == 2:
                    cost += 2
                elif c > 2:
                    cost += 1
                total = base + k + cost
                if dp[j + 1] is None or total < dp[j + 1]:
                    dp[j + 1] = total
        out.append(str(dp[n]))
    sys.stdout.write("\n".join(out) + "\n")


main()
