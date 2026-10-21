import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        d = y - x
        if d == 0:
            out.append("0")
        elif d < 0:
            out.append("1" if d % 2 == 0 else "2")
        elif d % 2:
            out.append("1")
        elif d % 4 == 2:
            out.append("2")               # 2a with a = d/2 odd
        else:
            out.append("3")               # 2a - b; two ups land on 2 mod 4
    sys.stdout.write("\n".join(out) + "\n")


main()
