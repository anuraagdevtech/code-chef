import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    c = int(data[0])
    pos = 1
    out = []
    for _ in range(c):
        n = int(data[pos])
        counts = Counter(data[pos + 1])
        pos += 2
        odds = sum(1 for v in counts.values() if v % 2)
        if n % 2 == 0:
            # k is even, so only k == 0 fails, and one edit lifts it to 2.
            out.append("0" if odds >= 2 else "1")
        elif odds >= 3:
            out.append("0")
        elif len(counts) == 1:
            # Nothing with an even count to draw from, so it takes two edits.
            out.append("2")
        else:
            out.append("1")
    sys.stdout.write("\n".join(out) + "\n")


main()
