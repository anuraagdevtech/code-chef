import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        # Input order is X, A, B: threshold first, then easy, then hard.
        x, a, b = map(int, data[1 + 3 * i:4 + 3 * i])
        out.append("Qualify" if a + 2 * b >= x else "NotQualify")
    sys.stdout.write("\n".join(out) + "\n")


main()
