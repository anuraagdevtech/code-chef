import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # z / (x * y) > 1 / 2  <=>  2 * z > x * y
        out.append("YES" if 2 * z > x * y else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
