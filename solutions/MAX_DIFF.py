import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, s = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Push one dish as high as the cap and the sum allow.
        hi = min(n, s)
        out.append(str(2 * hi - s))
    sys.stdout.write("\n".join(out) + "\n")


main()
