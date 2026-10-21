import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, k = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        counts = Counter(int(x) for x in data[pos + 3:pos + 3 + n])
        pos += 3 + n
        # Everything below K is mandatory; every copy of K is unusable; the
        # rest is free padding.
        ok = all(counts[v] for v in range(k)) and k <= m <= n - counts[k]
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
