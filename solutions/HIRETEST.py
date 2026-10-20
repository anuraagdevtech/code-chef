import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        x, y = int(data[pos + 2]), int(data[pos + 3])
        rows = data[pos + 4:pos + 4 + n]
        pos += 4 + n
        res = []
        for row in rows:
            full, partial = row.count(b"F"), row.count(b"P")
            # The fallback needs exactly x - 1 full solves, not merely fewer.
            ok = full >= x or (full == x - 1 and partial >= y)
            res.append("1" if ok else "0")
        out.append("".join(res))        # one line of digits, no separators
    sys.stdout.write("\n".join(out) + "\n")


main()
