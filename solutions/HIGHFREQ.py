import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(data[pos + 1:pos + 1 + n]).most_common(2)
        pos += 1 + n
        top = counts[0][1]
        runner = counts[1][1] if len(counts) > 1 else 0
        # Split the leader as evenly as possible; the runner-up is untouched.
        half = (top + 1) // 2
        out.append(str(half if half > runner else runner))
    sys.stdout.write("\n".join(out) + "\n")


main()
