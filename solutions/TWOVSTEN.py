import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # Doubling supplies factors of 2 but never a factor of 5.
        if x % 10 == 0:
            out.append("0")
        elif x % 5 == 0:
            out.append("1")
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
