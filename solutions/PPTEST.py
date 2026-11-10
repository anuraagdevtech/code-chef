"""CodeChef PPTEST — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,w = int(next(it)),int(next(it))
        dp = [0]*(w+1)
        for _ in range(n):
            c,p,t = int(next(it)),int(next(it)),int(next(it))
            points = c*p
            for time in range(w,t-1,-1):
                dp[time] = max(dp[time],dp[time-t]+points)
        out.append(str(dp[w]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
