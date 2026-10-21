import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if n > 1 and k == 1:
            # Prefixes 1 and N are always good, so one is impossible.
            out.append("-1")
            continue
        # Unit jumps first, then one descending run so no prefix in between
        # has its maximum equal to its length.
        head = list(range(1, k))
        tail = list(range(n, k - 1, -1))
        out.append(" ".join(map(str, head + tail)))
    sys.stdout.write("\n".join(out) + "\n")


main()
