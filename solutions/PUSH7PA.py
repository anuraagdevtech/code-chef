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
        # Every tower on the route started at the same height, so a height
        # occurring c times carries Pushpa to h + c - 1.
        out.append(str(max(h + c - 1 for h, c in counts.items())))
    sys.stdout.write("\n".join(out) + "\n")


main()
