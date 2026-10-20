import sys

# Clockwise from the starting heading, so index 0 is the initial direction.
DIRS = ("North", "East", "South", "West")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = [DIRS[int(data[1 + i]) % 4] for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
