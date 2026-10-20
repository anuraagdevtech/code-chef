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
        pairs = []
        for length, c in counts.items():
            # Four or more of a length supplies both sides, forming a square.
            pairs.extend([length] * (c // 2))
        pairs.sort(reverse=True)
        out.append(str(pairs[0] * pairs[1]) if len(pairs) >= 2 else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
