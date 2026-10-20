import sys

# Must be descending: greedy takes the largest note that still fits.
NOTES = (100, 50, 10, 5, 2, 1)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        count = 0
        for d in NOTES:
            count += n // d
            n %= d
        out.append(str(count))
    sys.stdout.write("\n".join(out) + "\n")


main()
