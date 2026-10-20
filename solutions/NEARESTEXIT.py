import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # dist left = x - 1, dist right = 100 - x; left wins iff x <= 50.
        out.append("LEFT" if x <= 50 else "RIGHT")
    sys.stdout.write("\n".join(out) + "\n")


main()
