"""CodeChef EVEDG — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, m = int(next(it)), int(next(it))
        degree = [0]*n
        edge = None
        for _ in range(m):
            u, v = int(next(it))-1, int(next(it))-1
            degree[u] += 1
            degree[v] += 1
            edge = u,v
        labels = [1]*n
        if m % 2 == 0:
            parts = 1
        else:
            odd = next((i for i,d in enumerate(degree) if d % 2),None)
            if odd is not None:
                parts = 2
                labels[odd] = 2
            else:
                parts = 3
                labels[edge[0]], labels[edge[1]] = 2,3
        out.append(str(parts))
        out.append(' '.join(map(str,labels)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
