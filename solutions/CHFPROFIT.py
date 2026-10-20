import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # Per-share margin times volume.
        out.append(str(x * (z - y)))
    sys.stdout.write("\n".join(out) + "\n")


main()
