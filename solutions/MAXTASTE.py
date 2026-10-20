import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = map(int, data[1 + 4 * i:5 + 4 * i])
        # The two picks are independent, so maximise each pair separately.
        out.append(str(max(a, b) + max(c, d)))
    sys.stdout.write("\n".join(out) + "\n")


main()
