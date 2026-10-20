import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = map(int, data[1 + 4 * i:5 + 4 * i])
        # Angles come in perimeter order, so A and C are opposite.
        # The total is fixed at 360, so B + D = 180 follows automatically.
        out.append("YES" if a + c == 180 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
