import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # Second largest of three is the median, duplicates included.
        out.append(str(sorted((a, b, c))[1]))
    sys.stdout.write("\n".join(out) + "\n")


main()
