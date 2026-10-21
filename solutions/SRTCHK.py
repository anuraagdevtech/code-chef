import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        b = [int(v) for v in data[pos + 1 + n:pos + 1 + 2 * n]]
        pos += 1 + 2 * n
        # One comparison tests both the multiset and the ordering.
        out.append("yes" if sorted(a) == b else "no")
    sys.stdout.write("\n".join(out) + "\n")


main()
