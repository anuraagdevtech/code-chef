import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, n = map(int, data[1 + 3 * i:4 + 3 * i])
        d = a ^ b
        if d == 0:
            out.append("0")
        elif d < n:
            out.append("1")
        elif d < (1 << (n - 1).bit_length()):
            # Reachable from the powers of two below n, in two picks.
            out.append("2")
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
