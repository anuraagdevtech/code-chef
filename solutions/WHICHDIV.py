import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        r = int(data[1 + i])
        # Bands are inclusive at their lower edge; test from the top down.
        out.append("1" if r >= 2000 else "2" if r >= 1600 else "3")
    sys.stdout.write("\n".join(out) + "\n")


main()
