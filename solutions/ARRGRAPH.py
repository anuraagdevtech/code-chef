"""CodeChef ARRGRAPH — standalone Python 3 solution."""
import sys
from math import gcd



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        seen = {0}
        stack = [0]
        while stack:
            v = stack.pop()
            for u in range(n):
                if u not in seen and gcd(a[u],a[v]) == 1:
                    seen.add(u)
                    stack.append(u)
        if len(seen) == n:
            out.append('0')
        else:
            a[0] = 43 if 47 in a else 47
            out.append('1')
        out.append(' '.join(map(str,a)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
