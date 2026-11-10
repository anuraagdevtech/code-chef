"""CodeChef HDELIVER — standalone Python 3 solution."""
import sys


class DSU:
    def __init__(self, n):
        self.p = [-1]*n
        self.count = n

    def find(self, x):
        p = self.p
        while p[x] >= 0:
            if p[p[x]] >= 0:
                p[x] = p[p[x]]
            x = p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        p = self.p
        if p[a] > p[b]:
            a, b = b, a
        p[a] += p[b]
        p[b] = a
        self.count -= 1
        return True



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,m = int(next(it)),int(next(it))
        d = DSU(n)
        for _ in range(m):
            d.union(int(next(it)),int(next(it)))
        q = int(next(it))
        for _ in range(q):
            u,v = int(next(it)),int(next(it))
            out.append('YO' if d.find(u) == d.find(v) else 'NO')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
