import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # x divides y, so the flight time is exact. Mario cannot fire early.
        out.append(str(max(0, z - y // x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
