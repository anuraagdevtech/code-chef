import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Fleeing thief closes the gap at 2 - 1 = 1 unit per second.
        out.append(str(abs(x - y)))
    sys.stdout.write("\n".join(out) + "\n")


main()
