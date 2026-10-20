import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        c = 21 - a - b
        # The third card is forced; it just has to be a card that exists.
        out.append(str(c) if 1 <= c <= 10 else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
