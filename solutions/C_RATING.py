import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        gap = max(0, y - x)
        # Each win is worth 8 rating, and a partial win is not a thing.
        out.append(str((gap + 7) // 8))
    sys.stdout.write("\n".join(out) + "\n")


main()
