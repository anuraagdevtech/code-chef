import sys
from heapq import heappush,heappop,heapreplace


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,budget,m = (int(next(tokens)) for _ in range(3))
        a = [int(next(tokens)) for _ in range(n)]
        intervals = []
        for _ in range(m):
            left,right,cost = (int(next(tokens)) for _ in range(3))
            intervals.append((left-1,right-1,cost))
        intervals.sort()
        active = []
        groups = {}
        index = 0
        for i,value in enumerate(a):
            while index < m and intervals[index][0] <= i:
                _,right,cost = intervals[index]
                heappush(active,(cost,right))
                index += 1
            while active and active[0][1] < i:
                heappop(active)
            if value >= 0 or not active:
                continue
            cost = active[0][0]
            if cost > budget:
                continue
            group = groups.setdefault(cost,[])
            gain = -value
            if len(group) < budget//cost:
                heappush(group,gain)
            elif gain > group[0]:
                heapreplace(group,gain)
        dp = [0]*(budget+1)
        for cost,group in groups.items():
            for gain in group:
                for capacity in range(budget,cost-1,-1):
                    dp[capacity] = max(dp[capacity],dp[capacity-cost]+gain)
        out.append(str(sum(a)+dp[budget]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
