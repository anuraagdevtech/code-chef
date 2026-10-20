import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Total coins earned, floored against the 100-coin bag price.
        out.append(str(x * y // 100))
    sys.stdout.write("\n".join(out) + "\n")


main()
