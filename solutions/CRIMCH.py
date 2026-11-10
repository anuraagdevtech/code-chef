"""CodeChef CRIMCH — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, m = int(next(it)), int(next(it))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u, v = int(next(it))-1, int(next(it))-1
            adj[u].append(v)
            adj[v].append(u)
        color = [-1]*n
        valid = True
        for start in range(n):
            if color[start] >= 0:
                continue
            color[start] = 0
            stack = [start]
            while stack:
                v = stack.pop()
                for u in adj[v]:
                    if color[u] < 0:
                        color[u] = color[v]^1
                        stack.append(u)
                    elif color[u] == color[v]:
                        valid = False
        out.append('YES' if valid else 'NO')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
