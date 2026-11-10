"""CodeChef GALACTIK — standalone Python 3 solution."""
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
    n, m = int(next(it)), int(next(it))
    d = DSU(n)
    for _ in range(m):
        d.union(int(next(it))-1,int(next(it))-1)
    best = {}
    for v in range(n):
        c = int(next(it))
        if c >= 0:
            root = d.find(v)
            best[root] = min(best.get(root,10**20),c)
    if d.count == 1:
        answer = 0
    elif len(best) != d.count:
        answer = -1
    else:
        answer = sum(best.values())+(d.count-2)*min(best.values())
    out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
