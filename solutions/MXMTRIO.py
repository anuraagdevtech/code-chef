import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # All values are positive, so take the widest difference and the
        # largest remaining element as the multiplier.
        out.append(str((a[-1] - a[0]) * a[-2]))
    sys.stdout.write("\n".join(out) + "\n")


main()
