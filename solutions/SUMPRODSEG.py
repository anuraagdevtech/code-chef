import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        lo, hi = x // 2, x - x // 2       # the shortest sum-segment
        # The most balanced factor pair is the one best able to clear it.
        small = 1
        for d in range(1, isqrt(y) + 1):
            if y % d == 0:
                small = d
        large = y // small
        if small > hi:
            out.append(f"{lo} {hi}")
            out.append(f"{small} {large}")
        elif large < lo:
            out.append(f"{small} {large}")
            out.append(f"{lo} {hi}")
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
