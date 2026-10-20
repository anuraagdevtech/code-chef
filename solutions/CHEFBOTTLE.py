import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, k = map(int, data[1 + 3 * i:4 + 3 * i])
        # Limited both by the water available and by the bottles owned.
        out.append(str(min(n, k // x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
