import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        vals = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        present = set(vals)
        # Only copies of M have to go; everything else is harmless.
        if all(str(v).encode() in present for v in range(1, m)):
            out.append(str(n - vals.count(str(m).encode())))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
