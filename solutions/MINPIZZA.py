import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # ceil(n * x / 4) in integer arithmetic.
        out.append(str((n * x + 3) // 4))
    sys.stdout.write("\n".join(out) + "\n")


main()
