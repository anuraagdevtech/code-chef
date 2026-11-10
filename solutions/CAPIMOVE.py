"""CodeChef CAPIMOVE — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        p = [int(next(it)) for _ in range(n)]
        adj = [[] for _ in range(n)]
        for _ in range(n-1):
            u, v = int(next(it))-1, int(next(it))-1
            adj[u].append(v)
            adj[v].append(u)
        order = sorted(range(n), key=p.__getitem__, reverse=True)
        marked = [-1]*n
        answer = []
        for v in range(n):
            marked[v] = v
            for u in adj[v]:
                marked[u] = v
            capital = 0
            for u in order:
                if marked[u] != v:
                    capital = u+1
                    break
            answer.append(capital)
        out.append(' '.join(map(str, answer)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
