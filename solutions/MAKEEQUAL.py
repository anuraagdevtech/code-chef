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
        # One move can raise every lagging element at once, so only the
        # widest gap matters - not the total shortfall.
        out.append(str(max(a) - min(a)))
    sys.stdout.write("\n".join(out) + "\n")


main()
