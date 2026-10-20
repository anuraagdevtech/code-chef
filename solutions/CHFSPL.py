import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p = list(map(int, data[1 + 3 * i:4 + 3 * i]))
        # Use two of three: drop the weakest, once, even if tied.
        out.append(str(sum(p) - min(p)))
    sys.stdout.write("\n".join(out) + "\n")


main()
