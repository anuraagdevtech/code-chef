import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, p = map(int, data[1 + 3 * i:4 + 3 * i])
        # 3x - (n - x) = 4x - n; the score may legitimately go negative.
        out.append("PASS" if 4 * x - n >= p else "FAIL")
    sys.stdout.write("\n".join(out) + "\n")


main()
