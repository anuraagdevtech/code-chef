import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # The best of three throws is the score.
        out.append(str(max(a, b, c)))
    sys.stdout.write("\n".join(out) + "\n")


main()
