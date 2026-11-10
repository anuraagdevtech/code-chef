"""CodeChef ARTBALAN — standalone Python 3 solution."""
import sys
from collections import Counter



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        s = next(it)
        n = len(s)
        counts = sorted(Counter(s).values(), reverse=True)
        counts += [0]*(26-len(counts))
        answer = n
        for distinct in range(1,27):
            if n % distinct == 0:
                target = n//distinct
                answer = min(answer, n-sum(min(c,target) for c in counts[:distinct]))
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
