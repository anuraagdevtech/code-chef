import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    pos = 1
    out = []
    for _ in range(k):
        n, t = int(data[pos]), float(data[pos + 1])
        xs = [float(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n

        def feasible(d):
            # Push everyone as far left as allowed: that leaves the most room.
            place = max(0.0, xs[0] - d)
            if place > xs[0] + d:
                return False
            for x in xs[1:]:
                place = max(place + t, x - d)
                if place > x + d:
                    return False
            return True

        lo, hi = 0.0, t * n + xs[-1] + 1.0
        for _ in range(100):
            mid = (lo + hi) / 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid
        out.append(f"{hi:.4f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
