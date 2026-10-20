import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s, x, y, z = map(int, data[1 + 4 * i:5 + 4 * i])
        free = s - x - y
        if free >= z:
            out.append("0")
        elif free + max(x, y) >= z:   # if deleting one, delete the bigger
            out.append("1")
        else:
            out.append("2")
    sys.stdout.write("\n".join(out) + "\n")


main()
