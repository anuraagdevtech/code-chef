import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        h = len(s) // 2
        # s[n-h:] skips the middle character when the length is odd.
        same = Counter(s[:h]) == Counter(s[len(s) - h:])
        out.append("YES" if same else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
