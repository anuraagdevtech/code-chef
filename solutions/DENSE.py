import sys

OPEN = 0x28


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        closes = n - s.count(OPEN)      # ')' still ahead of the split
        opens = 0
        best = 0
        # Split before each position: take opens from the left, closes right.
        for c in s:
            if c == OPEN:
                opens += 1
            else:
                closes -= 1
            best = max(best, opens if opens < closes else closes)
        out.append(str(n - 2 * best))
    sys.stdout.write("\n".join(out) + "\n")


main()
