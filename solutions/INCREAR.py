import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if x <= y:
            ops = y - x                  # only +1 on x can help
        else:
            d = x - y
            # +2 steps preserve parity, so an odd gap needs a +1 as well.
            ops = d // 2 if d % 2 == 0 else (d + 3) // 2
        out.append(str(ops))
    sys.stdout.write("\n".join(out) + "\n")


main()
