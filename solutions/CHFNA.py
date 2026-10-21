import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Matching bits cost nothing, differing bits cost 2^b whatever A does.
        out.append(str(x ^ y))
    sys.stdout.write("\n".join(out) + "\n")


main()
