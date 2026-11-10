"""CodeChef CHEFHAM — standalone Python 3 solution."""
import sys
from collections import Counter



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        indices = sorted(range(n), key=a.__getitem__)
        shift = max(Counter(a).values())
        b = [0]*n
        for i, idx in enumerate(indices):
            b[idx] = a[indices[(i+shift)%n]]
        out.append(str(sum(x != y for x,y in zip(a,b))))
        out.append(' '.join(map(str,b)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
