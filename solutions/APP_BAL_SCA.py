import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        m, n = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # The balance only bisects, so the finest piece is M's odd part.
        unit = m
        while unit % 2 == 0:
            unit //= 2
        out.append("YES" if n <= m and n % unit == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
