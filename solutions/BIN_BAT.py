import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, a, b = map(int, data[1 + 3 * i:4 + 3 * i])
        # n is a power of two, so bit_length gives an exact log2.
        rounds = n.bit_length() - 1
        # Breaks sit between rounds, so there is one fewer of them.
        out.append(str(rounds * a + (rounds - 1) * b))
    sys.stdout.write("\n".join(out) + "\n")


main()
