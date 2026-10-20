import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Every round uses exactly n tiles and none may be left over.
        out.append("YES" if x % n == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
