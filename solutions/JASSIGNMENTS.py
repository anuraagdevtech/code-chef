import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # Starts at x, needs 3 hours, must land no later than 10.
        out.append("Yes" if x + 3 <= 10 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
