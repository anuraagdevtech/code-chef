import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted(int(x) for x in data[pos + 1:pos + 1 + n])
        b = sorted(int(x) for x in data[pos + 1 + n:pos + 1 + 2 * n])
        pos += 1 + 2 * n
        m = (n + 1) // 2
        # Top m of each side, paired in opposite order to lift the minimum.
        out.append(str(min(a[n - m + i] + b[n - 1 - i] for i in range(m))))
    sys.stdout.write("\n".join(out) + "\n")


main()
