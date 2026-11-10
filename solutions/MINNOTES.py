"""CodeChef MINNOTES — standalone Python 3 solution."""
import sys
from math import gcd



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        if n == 1:
            out.append('1')
            continue
        pref = [0] * (n+1)
        for i, x in enumerate(a):
            pref[i+1] = gcd(pref[i], x)
        total, suffix = sum(a), 0
        answer = total // pref[n]
        for i in range(n-1, -1, -1):
            g = gcd(pref[i], suffix)
            answer = min(answer, (total-a[i]) // g + 1)
            suffix = gcd(suffix, a[i])
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
