import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # k = 0 is allowed by the constraints and would crash the modulo.
        out.append(str(n if k == 0 else n % k))
    sys.stdout.write("\n".join(out) + "\n")


main()
