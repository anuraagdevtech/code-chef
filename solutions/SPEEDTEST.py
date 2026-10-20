import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, x, b, y = map(int, data[1 + 4 * i:5 + 4 * i])
        # a/x vs b/y, cross-multiplied so the comparison stays exact.
        alice, bob = a * y, b * x
        out.append("ALICE" if alice > bob else "BOB" if bob > alice else "EQUAL")
    sys.stdout.write("\n".join(out) + "\n")


main()
