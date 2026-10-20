import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # As many y-jumps as fit, then single steps for the remainder.
        out.append(str(x // y + x % y))
    sys.stdout.write("\n".join(out) + "\n")


main()
