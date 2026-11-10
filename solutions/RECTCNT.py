"""Group vertical sides by their pair of y coordinates."""
import sys
from collections import Counter


def solve():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for n in it:
        if n == 0:
            break
        columns = {}
        sides = Counter()
        answer = 0
        for _ in range(n):
            x, y = next(it), next(it)
            if x in columns:
                pair = tuple(sorted((columns[x], y)))
                answer += sides[pair]
                sides[pair] += 1
            else:
                columns[x] = y
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    solve()
