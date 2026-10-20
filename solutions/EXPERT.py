import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # y / x >= 1 / 2  <=>  2 * y >= x   ("at least", so not strict)
        out.append("YES" if 2 * y >= x else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
