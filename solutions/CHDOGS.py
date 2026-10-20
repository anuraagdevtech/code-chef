import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s, v = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Symmetry keeps the chase angle at 120 degrees, so the gap closes at
        # a constant v - v*cos(120) = 1.5v.
        out.append(f"{2 * s / (3 * v):.9f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
