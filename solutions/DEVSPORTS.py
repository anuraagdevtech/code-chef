import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        z, y, a, b, c = map(int, data[1 + 5 * i:6 + 5 * i])
        # Spending down to exactly zero still counts.
        out.append("YES" if z - y >= a + b + c else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
