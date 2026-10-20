import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, p, x, y = map(int, data[pos:pos + 4])
        a = data[pos + 4:pos + 4 + n]
        pos += 4 + n
        # Everyone up to and including Chef at position p must be served.
        total = sum(y if v == b"1" else x for v in a[:p])
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
