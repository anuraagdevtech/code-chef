import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        m,n = int(next(tokens))+1,int(next(tokens))+1
        grid = b''.join(next(tokens) for _ in range(m))
        target = int(next(tokens))
        size = m*n
        start = grid.index(42)
        graph = [[] for _ in range(size)]
        value = [c-48 if 48 <= c <= 57 else 0 for c in grid]
        for u,c in enumerate(grid):
            if c == 35:
                continue
            r,col = divmod(u,n)
            for v in (u-n if r else -1,u+n if r+1 < m else -1,
                      u-1 if col else -1,u+1 if col+1 < n else -1):
                if v >= 0 and grid[v] != 35:
                    graph[u].append(v)
        seen = bytearray((target+1)*size)
        seen[start] = 1
        queue = deque([start])
        steps = 0
        answer = -1
        while queue and answer == -1:
            for _ in range(len(queue)):
                state = queue.popleft()
                total,u = divmod(state,size)
                if total == target:
                    answer = steps
                    break
                for v in graph[u]:
                    next_total = total+value[v]
                    if next_total <= target:
                        next_state = next_total*size+v
                        if not seen[next_state]:
                            seen[next_state] = 1
                            queue.append(next_state)
            steps += 1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
