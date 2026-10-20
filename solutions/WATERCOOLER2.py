import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Largest m with m * x < y. The -1 is what makes it strict.
        out.append(str((y - 1) // x))
    sys.stdout.write("\n".join(out) + "\n")


main()
