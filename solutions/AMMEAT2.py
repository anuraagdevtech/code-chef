import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if k == 1:
            # No pairs to check, so any single plate is fine.
            out.append("1")
        elif 2 * k <= n:
            # All even, so every pair shares the factor 2.
            out.append(" ".join(str(2 * j) for j in range(1, k + 1)))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
