import sys
from itertools import combinations


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        w, x, y, z = map(int, data[1 + 4 * i:5 + 4 * i])
        weights = (x, y, z)
        # Every non-empty subset; weights only add, they never subtract.
        ok = any(sum(c) == w
                 for r in (1, 2, 3)
                 for c in combinations(weights, r))
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
