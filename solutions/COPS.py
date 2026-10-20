import sys

HOUSES = 100


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        m, x, y = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        cops = [int(v) for v in data[pos + 3:pos + 3 + m]]
        pos += 3 + m
        reach = x * y
        covered = [False] * (HOUSES + 1)
        for c in cops:
            # Clamp to the street; ranges from different cops may overlap.
            lo = max(1, c - reach)
            hi = min(HOUSES, c + reach)
            for h in range(lo, hi + 1):
                covered[h] = True
        out.append(str(sum(1 for h in range(1, HOUSES + 1) if not covered[h])))
    sys.stdout.write("\n".join(out) + "\n")


main()
