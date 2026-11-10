"""CodeChef N1 — standalone Python 3 solution."""
import sys
from collections import deque



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        grid = [next(it) for _ in range(n)]
        treasures = [r*n+c for r in range(n) for c in range(n) if grid[r][c] == 42]
        points = [0]+treasures+[n*n-1]
        distances = []
        for start in points:
            dist = [-1]*(n*n)
            dist[start] = 0
            queue = deque([start])
            while queue:
                v = queue.popleft()
                r,c = divmod(v,n)
                for rr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if 0 <= rr < n and 0 <= cc < n:
                        u = rr*n+cc
                        if grid[rr][cc] != 35 and dist[u] < 0:
                            dist[u] = dist[v]+1
                            queue.append(u)
            distances.append([dist[p] for p in points])
        if any(x < 0 for x in distances[0]):
            out.append('-1')
            continue
        count = len(treasures)
        if count == 0:
            out.append(str(distances[0][-1]))
            continue
        full = (1 << count)-1
        dp = [[10**9]*count for _ in range(full+1)]
        for j in range(count):
            dp[1 << j][j] = distances[0][j+1]
        for mask in range(1,full+1):
            for last in range(count):
                value = dp[mask][last]
                if value == 10**9:
                    continue
                remaining = full^mask
                while remaining:
                    bit = remaining & -remaining
                    nxt = bit.bit_length()-1
                    target = dp[mask|bit]
                    target[nxt] = min(target[nxt],value+distances[last+1][nxt+1])
                    remaining -= bit
        out.append(str(min(dp[full][j]+distances[j+1][-1] for j in range(count))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
