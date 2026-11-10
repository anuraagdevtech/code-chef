"""CodeChef SNSOCIAL — standalone Python 3 solution."""
import sys
from collections import deque



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, m = int(next(it)), int(next(it))
        a = [int(next(it)) for _ in range(n*m)]
        greatest = max(a)
        dist = [-1]*(n*m)
        queue = deque()
        for i,x in enumerate(a):
            if x == greatest:
                dist[i] = 0
                queue.append(i)
        answer = 0
        while queue:
            v = queue.popleft()
            r, c = divmod(v,m)
            for rr in range(max(0,r-1),min(n,r+2)):
                for cc in range(max(0,c-1),min(m,c+2)):
                    u = rr*m+cc
                    if dist[u] < 0:
                        dist[u] = dist[v]+1
                        answer = max(answer,dist[u])
                        queue.append(u)
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
