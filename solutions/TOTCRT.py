import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        totals = defaultdict(int)
        # Three blocks of n entries; a code may appear in several divisions.
        for _ in range(3 * n):
            totals[data[pos]] += int(data[pos + 1])
            pos += 2
        out.append(" ".join(map(str, sorted(totals.values()))))
    sys.stdout.write("\n".join(out) + "\n")


main()
