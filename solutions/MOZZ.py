import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, r = map(int, data[1 + 3 * i:4 + 3 * i])
        sticks = x + r // 30          # r is guaranteed to be a multiple of 30
        # The final plate may be left unfinished but was still ordered.
        out.append(str((sticks + y - 1) // y))
    sys.stdout.write("\n".join(out) + "\n")


main()
