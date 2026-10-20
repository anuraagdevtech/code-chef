import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Healthy pack together; each infected costs a gap plus a room, except
        # that with nobody healthy the leading gap is not needed.
        out.append(str(x + y - (1 if x == y else 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
