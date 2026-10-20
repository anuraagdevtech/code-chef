import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, x, y = map(int, data[1 + 4 * i:5 + 4 * i])
        # Hot only warms and cold only cools: reachable range is [a - y, a + x].
        out.append("YES" if a - y <= b <= a + x else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
