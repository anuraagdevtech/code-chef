import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Income 50n, costs 20 + 20 + 30 = 70%, so profit is 30% of 50n.
        out.append(str(15 * n))
    sys.stdout.write("\n".join(out) + "\n")


main()
