import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        best = None
        v, steps = a, 0
        # Any optimal route halves first, then doubles: doubling cannot undo
        # the information that rounding down has already discarded.
        while v > 0:
            if v <= b and b % v == 0:
                q = b // v
                if q & (q - 1) == 0:          # q is a power of two
                    cost = steps + q.bit_length() - 1
                    if best is None or cost < best:
                        best = cost
            v //= 2
            steps += 1
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
