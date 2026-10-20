import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # One item is free per complete block of three.
        out.append(str((n - n // 3) * x))
    sys.stdout.write("\n".join(out) + "\n")


main()
