import sys
from bisect import bisect_right


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        tops = []
        for v in data[pos + 1:pos + 1 + n]:
            d = int(v)
            # First top strictly greater than d; the list stays sorted after
            # the overwrite, so no re-sorting is ever needed.
            k = bisect_right(tops, d)
            if k == len(tops):
                tops.append(d)
            else:
                tops[k] = d
        pos += 1 + n
        out.append(" ".join(map(str, [len(tops)] + tops)))
    sys.stdout.write("\n".join(out) + "\n")


main()
