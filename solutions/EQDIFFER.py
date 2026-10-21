import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # Keep all copies of one value, or keep any two elements.
        keep = max(max(counts.values()), min(n, 2))
        out.append(str(n - keep))
    sys.stdout.write("\n".join(out) + "\n")


main()
