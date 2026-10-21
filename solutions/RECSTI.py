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
        added = sum(c & 1 for c in counts.values())      # orphan per odd length
        pairs = sum((c + 1) // 2 for c in counts.values())
        # A leftover pair needs a whole new pair to square off with.
        out.append(str(added + 2 * (pairs & 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
