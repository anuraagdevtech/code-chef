import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, k = map(int, data[1 + 3 * i:4 + 3 * i])
        d = abs(a - b)
        # Steps are "at most K", so the last one can be short.
        out.append(str((d + k - 1) // k))
    sys.stdout.write("\n".join(out) + "\n")


main()
