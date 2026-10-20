import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = map(int, data[1 + 4 * i:5 + 4 * i])
        # Goals never decrease, and the two teams move independently.
        out.append("POSSIBLE" if c >= a and d >= b else "IMPOSSIBLE")
    sys.stdout.write("\n".join(out) + "\n")


main()
