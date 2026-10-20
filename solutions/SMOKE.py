import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, y = map(int, data[1 + 3 * i:4 + 3 * i])
        best = None
        # At most ceil(n / 100) buses are ever worth taking.
        for buses in range((n + 99) // 100 + 1):
            rest = max(0, n - 100 * buses)
            cost = buses * x + (rest + 3) // 4 * y
            if best is None or cost < best:
                best = cost
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
