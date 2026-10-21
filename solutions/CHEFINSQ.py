import sys
from math import comb


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(x) for x in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        cut = a[k - 1]
        # Only the copies of the boundary value are interchangeable.
        out.append(str(comb(a.count(cut), a[:k].count(cut))))
    sys.stdout.write("\n".join(out) + "\n")


main()
