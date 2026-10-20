import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        xa, xb, big_xa, big_xb = map(int, data[1 + 4 * i:5 + 4 * i])
        # Water and pulp come from different coconuts; both divisions are exact.
        out.append(str(big_xa // xa + big_xb // xb))
    sys.stdout.write("\n".join(out) + "\n")


main()
