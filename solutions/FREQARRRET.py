import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        b = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        if any(c % f for f, c in Counter(b).items()):
            out.append("-1")
            continue
        label = 0
        open_label = {}        # frequency -> label of the group still filling
        filled = {}
        a = []
        for f in b:
            if f not in open_label:
                label += 1     # a fresh label is the smallest unused value
                open_label[f] = label
                filled[f] = 0
            a.append(open_label[f])
            filled[f] += 1
            if filled[f] == f:
                del open_label[f]
        out.append(" ".join(map(str, a)))
    sys.stdout.write("\n".join(out) + "\n")


main()
