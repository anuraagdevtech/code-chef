import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # n is odd, so the two sequences meet at the middle hoop, which the
        # first player reaches first.
        out.append(str((n + 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
