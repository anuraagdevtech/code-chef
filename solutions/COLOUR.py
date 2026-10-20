import sys
from itertools import product


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        best = 0
        # yellow = red + green, cyan = green + blue, magenta = red + blue
        for yel, cya, mag in product((0, 1), repeat=3):
            r, g, b = x - (yel + mag), y - (yel + cya), z - (cya + mag)
            if r < 0 or g < 0 or b < 0:
                continue
            # Primaries still in hand, plus the secondaries actually made.
            total = (r >= 1) + (g >= 1) + (b >= 1) + yel + cya + mag
            best = max(best, total)
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
