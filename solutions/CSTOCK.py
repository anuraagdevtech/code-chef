import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s, a, b, c = map(int, data[1 + 4 * i:5 + 4 * i])
        # Scale the whole comparison by 100 so no division or float is needed.
        price100 = s * (100 + c)
        out.append("Yes" if 100 * a <= price100 <= 100 * b else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
