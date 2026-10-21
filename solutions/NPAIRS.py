import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for case in range(t):
        s = data[2 + 2 * case]
        # j - i = |S_j - S_i| holds iff S-i matches, or S+i matches.
        down = Counter(d - i for i, d in enumerate(s))
        up = Counter(d + i for i, d in enumerate(s))
        total = sum(c * (c - 1) // 2 for c in down.values())
        total += sum(c * (c - 1) // 2 for c in up.values())
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
