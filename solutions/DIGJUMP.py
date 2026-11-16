import sys
from collections import deque


def main() -> None:
    s = sys.stdin.buffer.read().strip()
    n = len(s)
    positions = [[] for _ in range(10)]
    for i,c in enumerate(s):
        positions[c-48].append(i)
    distance = [-1]*n
    distance[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        if u == n-1:
            print(distance[u])
            return
        digit = s[u]-48
        group = positions[digit]
        positions[digit] = []
        for v in group:
            if distance[v] == -1:
                distance[v] = distance[u]+1
                queue.append(v)
        for v in (u-1,u+1):
            if 0 <= v < n and distance[v] == -1:
                distance[v] = distance[u]+1
                queue.append(v)

if __name__ == '__main__':
    main()
