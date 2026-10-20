import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        if n == 2:
            # One difference, nothing to cancel it against.
            out.append("-1")
        elif n % 2:
            # n - 1 differences of 1, an even count, so they cancel.
            out.append(" ".join(map(str, range(1, n + 1))))
        else:
            # Differences 1, 2, 3 cancel; the remaining n - 4 ones pair off.
            rest = range(4, n + 1)
            out.append(" ".join(map(str, (2, 3, 1, *rest))))
    sys.stdout.write("\n".join(out) + "\n")


main()
