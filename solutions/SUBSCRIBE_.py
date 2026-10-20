import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # ceil(n / 6) without floats: (n + 6 - 1) // 6
        out.append(str((n + 5) // 6 * x))
    sys.stdout.write("\n".join(out) + "\n")


main()
