import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # Two lower bounds collapse to their max; feasible if it clears b.
        out.append("Yes" if max(a, c) <= b else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
