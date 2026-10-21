import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # Points from different values never collide, so each value is capped
        # independently by its copies and by its v - 1 possible splits.
        out.append(str(sum(min(c, v - 1) for v, c in counts.items())))
    sys.stdout.write("\n".join(out) + "\n")


main()
