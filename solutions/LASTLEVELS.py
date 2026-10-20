import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # Breaks sit between blocks of 3, so none follows the final level.
        out.append(str(x * y + z * ((x - 1) // 3)))
    sys.stdout.write("\n".join(out) + "\n")


main()
