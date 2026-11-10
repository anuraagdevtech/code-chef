"""CodeChef DIGITOP — standalone Python 3 solution."""
import sys
from collections import Counter



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, k = int(next(it)), int(next(it))
        a = [next(it) for _ in range(n)]
        b = [next(it) for _ in range(n)]
        if any(len(x) != len(y) for x,y in zip(a,b)):
            out.append('NO')
            continue
        ca, cb = Counter(b''.join(a)), Counter(b''.join(b))
        cost = sum(max(0, cb[d]-ca[d]) for d in cb)
        out.append('YES' if cost <= k else 'NO')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
