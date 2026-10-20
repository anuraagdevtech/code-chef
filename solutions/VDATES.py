import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        d, l, r = map(int, data[1 + 3 * i:4 + 3 * i])
        # Both ends of the window are inclusive.
        out.append("Too Early" if d < l else "Too Late" if d > r else "Take second dose now")
    sys.stdout.write("\n".join(out) + "\n")


main()
