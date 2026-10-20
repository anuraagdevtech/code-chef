import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, a, b, c = map(int, data[1 + 4 * i:5 + 4 * i])
        # Every dish takes one vegetable plus either a fruit or a fish.
        out.append("YES" if min(b, a + c) >= n else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
