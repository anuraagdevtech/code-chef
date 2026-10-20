import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, x = map(int, data[1 + 3 * i:4 + 3 * i])
        # x is guaranteed to divide b - a, so this is exact.
        out.append(str((b - a) // x))
    sys.stdout.write("\n".join(out) + "\n")


main()
