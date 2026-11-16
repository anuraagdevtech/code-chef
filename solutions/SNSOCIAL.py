import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, m = int(next(tokens)), int(next(tokens))
        a = [int(next(tokens)) for _ in range(n*m)]
        maximum = max(a)
        distance = [-1]*(n*m)
        queue = deque()
        for i,v in enumerate(a):
            if v == maximum:
                distance[i] = 0
                queue.append(i)
        answer = 0
        while queue:
            u = queue.popleft()
            r,c = divmod(u,m)
            answer = distance[u]
            for rr in range(max(0,r-1), min(n,r+2)):
                for cc in range(max(0,c-1), min(m,c+2)):
                    v = rr*m+cc
                    if distance[v] == -1:
                        distance[v] = distance[u]+1
                        queue.append(v)
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
