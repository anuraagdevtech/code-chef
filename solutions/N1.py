import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        grid = [next(tokens) for _ in range(n)]
        treasures = [r*n+c for r in range(n) for c in range(n) if grid[r][c] == 42]
        points = [0]+treasures+[n*n-1]
        k = len(treasures)
        distances = []
        for start in points:
            distance = [-1]*(n*n)
            distance[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                r,c = divmod(u,n)
                for v in (u-n if r else -1,u+n if r+1 < n else -1,
                          u-1 if c else -1,u+1 if c+1 < n else -1):
                    if v >= 0 and distance[v] == -1 and grid[v//n][v%n] != 35:
                        distance[v] = distance[u]+1
                        queue.append(v)
            distances.append([distance[v] for v in points])
        if any(d < 0 for d in distances[0]):
            out.append('-1')
            continue
        if k == 0:
            out.append(str(distances[0][-1]))
            continue
        infinity = 10**9
        dp = [[infinity]*k for _ in range(1 << k)]
        for j in range(k):
            dp[1 << j][j] = distances[0][j+1]
        full = (1 << k)-1
        for mask in range(1,full+1):
            for j in range(k):
                current = dp[mask][j]
                if current == infinity:
                    continue
                todo = full^mask
                while todo:
                    bit = todo&-todo
                    v = bit.bit_length()-1
                    target = mask|bit
                    dp[target][v] = min(dp[target][v],current+distances[j+1][v+1])
                    todo -= bit
        out.append(str(min(dp[full][j]+distances[j+1][-1] for j in range(k))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
