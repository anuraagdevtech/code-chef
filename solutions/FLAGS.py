import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Two 3-stripe paths, two triangles, and one K4-minus-an-edge.
        total = (2 * n * (n - 1) ** 2
                 + 2 * n * (n - 1) * (n - 2)
                 + n * (n - 1) * (n - 2) ** 2)
        out.append(str(max(0, total)))
    sys.stdout.write("\n".join(out) + "\n")


main()
