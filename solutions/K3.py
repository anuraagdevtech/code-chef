"""CodeChef K3 — standalone Python 3 solution."""
import sys
from collections import deque



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        rows,cols = int(next(it))+1,int(next(it))+1
        grid = b''.join(next(it) for _ in range(rows))
        target = int(next(it))
        cells = rows*cols
        start = grid.index(42)
        seen = bytearray(cells*(target+1))
        seen[start] = 1
        queue = deque([start])
        steps,answer = 0,-1
        while queue and answer < 0:
            for _ in range(len(queue)):
                state = queue.popleft()
                total,v = divmod(state,cells)
                if total == target:
                    answer = steps
                    break
                r,c = divmod(v,cols)
                for rr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if not (0 <= rr < rows and 0 <= cc < cols):
                        continue
                    u = rr*cols+cc
                    char = grid[u]
                    if char == 35:
                        continue
                    newtotal = total+(char-48 if 48 <= char <= 57 else 0)
                    if newtotal > target:
                        continue
                    nxt = newtotal*cells+u
                    if not seen[nxt]:
                        seen[nxt] = 1
                        queue.append(nxt)
            steps += 1
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
