import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = data[1 + i].decode()
        # int() also strips the leading zeros that reversing can create.
        out.append(str(int(n[::-1])))
    sys.stdout.write("\n".join(out) + "\n")


main()
