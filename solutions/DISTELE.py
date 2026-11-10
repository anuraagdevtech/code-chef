"""CodeChef DISTELE — standalone Python 3 solution."""
import sys
from collections import Counter



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        counts = Counter(next(it) for _ in range(n))
        answer = 1
        for count in counts.values():
            answer = answer * (count+1) % 1000000007
        out.append(str((answer-1) % 1000000007))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
