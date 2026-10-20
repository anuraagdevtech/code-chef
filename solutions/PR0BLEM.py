import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Every move changes n - m by an even amount, so its parity is fixed.
        out.append("YES" if (n - m) % 2 == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
