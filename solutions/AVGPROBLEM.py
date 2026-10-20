import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # (a + b) / 2 > c  <=>  a + b > 2 * c, kept in integers.
        out.append("YES" if a + b > 2 * c else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
