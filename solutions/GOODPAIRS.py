import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = data[pos + 1:pos + 1 + n]
        b = data[pos + 1 + n:pos + 1 + 2 * n]
        pos += 1 + 2 * n
        seen = Counter()
        total = 0
        for x, y in zip(a, b):
            # Look for earlier indices whose key is this one reversed.
            total += seen[(y, x)]
            seen[(x, y)] += 1
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
