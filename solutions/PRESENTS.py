import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # One gift is free per complete block of five.
        out.append(str(n - n // 5))
    sys.stdout.write("\n".join(out) + "\n")


main()
