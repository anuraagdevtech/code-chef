"""CodeChef PALPALS — standalone Python 3 solution."""
import sys
from collections import Counter



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        counts = Counter(next(it))
        pairs = sum(c//2 for c in counts.values())
        odd = sum(c%2 for c in counts.values())
        out.append('YES' if pairs >= odd else 'NO')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
