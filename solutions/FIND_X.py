import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = (int(data[1 + 4 * i]), int(data[2 + 4 * i]),
                      int(data[3 + 4 * i]), int(data[4 + 4 * i]))
        r = a % b
        small = b if b < d else d
        if r + 1 < small:
            out.append("1")              # still inside the current window
        else:
            # The window ends here, so jump to the start of the next one.
            out.append(str(b // gcd(b, d) * d - r))
    sys.stdout.write("\n".join(out) + "\n")


main()
