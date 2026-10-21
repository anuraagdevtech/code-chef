import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(int(x) for x in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        top = max(counts)
        # Two arms, so twice is the ceiling; the peak cannot be shared.
        if max(counts.values()) > 2 or counts[top] != 1:
            out.append("NO")
            continue
        values = sorted(counts)
        doubled = [v for v in reversed(values) if counts[v] == 2]
        out.append("YES")
        out.append(" ".join(map(str, values + doubled)))
    sys.stdout.write("\n".join(out) + "\n")


main()
