import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        vals = []
        if n % 2:
            vals.append(x)              # the centre contributes the mean itself
        # Each pair (x - d, x + d) averages to x, and offsets stay distinct.
        for d in range(1, n // 2 + 1):
            vals.append(x - d)
            vals.append(x + d)
        out.append(" ".join(map(str, vals)))
    sys.stdout.write("\n".join(out) + "\n")


main()
