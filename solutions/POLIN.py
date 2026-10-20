import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        # Vertical and horizontal lines are counted on separate axes, so a
        # shared numeric value does not merge them.
        xs = set(data[pos:pos + 2 * n:2])
        ys = set(data[pos + 1:pos + 2 * n:2])
        pos += 2 * n
        out.append(str(len(xs) + len(ys)))
    sys.stdout.write("\n".join(out) + "\n")


main()
