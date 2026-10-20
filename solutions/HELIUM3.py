import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, x, y = map(int, data[1 + 4 * i:5 + 4 * i])
        # Total demand a * b against total supply x * y.
        out.append("Yes" if x * y >= a * b else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
