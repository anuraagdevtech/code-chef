import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, want, rod = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        counts = Counter(int(x) for x in data[pos + 3:pos + 3 + n])
        pos += 3 + n
        # Only matched twins can go on the bar; odd leftovers are dead weight.
        load = rod + 2 * sum(w * (c // 2) for w, c in counts.items())
        out.append("YES" if load >= want else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
