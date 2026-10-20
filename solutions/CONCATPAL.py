import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        a, b = data[pos + 2], data[pos + 3]
        pos += 4
        if n > m:
            a, b = b, a
        ca, cb = Counter(a), Counter(b)
        # Every position of the shorter side mirrors into the longer one.
        if any(cb[ch] < cnt for ch, cnt in ca.items()):
            out.append("NO")
            continue
        # What is left of the longer side forms the palindromic centre.
        rest = cb - ca
        out.append("YES" if sum(1 for v in rest.values() if v % 2) <= 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
