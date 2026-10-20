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
        # Keep whichever value is already most common; fix the rest one by one.
        out.append(str(n - max(counts.values())))
    sys.stdout.write("\n".join(out) + "\n")


main()
