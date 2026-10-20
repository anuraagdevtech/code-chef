import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Boasts when strictly more than half the class scores no higher,
        # counting yourself: 2 * c > n.
        boasters = sum(1 for x in a if 2 * sum(1 for y in a if y <= x) > n)
        out.append(str(boasters))
    sys.stdout.write("\n".join(out) + "\n")


main()
