import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    out = []
    for i in range(q):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        d = abs(a - b)
        # Difference of 2 is always a rail; difference of 1 is a rung only
        # when the lower endpoint is odd.
        road = d == 2 or (d == 1 and min(a, b) % 2 == 1)
        out.append("YES" if road else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
