import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        top = max(Counter(data[pos + 1:pos + 1 + n]).values())
        pos += 1 + n
        if top == n:
            out.append("0")          # every element is already a valid list
        elif top >= 2:
            # One list buries all the other values; the rest stay singletons.
            out.append(str(n - top + 1))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
