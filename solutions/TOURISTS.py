"""CodeChef TOURISTS — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    n, m = int(next(it)), int(next(it))
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = int(next(it))-1, int(next(it))-1
        adj[u].append((v,i))
        adj[v].append((u,i))
    used = bytearray(m)
    answer = [None]*m
    stack = [0]
    seen = bytearray(n)
    seen[0] = 1
    while stack:
        v = stack[-1]
        while adj[v] and used[adj[v][-1][1]]:
            adj[v].pop()
        if not adj[v]:
            stack.pop()
            continue
        u,i = adj[v].pop()
        used[i] = 1
        seen[u] = 1
        answer[i] = (v+1,u+1)
        stack.append(u)
    degree = [0]*n
    for edge in answer:
        if edge is not None:
            degree[edge[0]-1] += 1
            degree[edge[1]-1] -= 1
    if not all(seen) or not all(used) or any(degree):
        out.append('NO')
    else:
        out.append('YES')
        out.extend(f'{u} {v}' for u,v in answer)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
