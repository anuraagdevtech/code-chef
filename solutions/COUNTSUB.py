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
        # f(l, r) telescopes to A_l - A_r, so a subarray is unstable exactly
        # when its endpoints differ.
        same = sum(c * (c - 1) // 2 for c in counts.values())
        out.append(str(n * (n - 1) // 2 - same))
    sys.stdout.write("\n".join(out) + "\n")


main()
