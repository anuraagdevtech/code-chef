import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Chef may already hold more candies than children, so clamp first.
        need = max(0, n - x)
        out.append(str((need + 3) // 4))
    sys.stdout.write("\n".join(out) + "\n")


main()
