import sys

STAR = 0x2A


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        rows = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # Manhattan distance is Chebyshev distance in (r+c, r-c).
        lo_u = lo_v = 1 << 60
        hi_u = hi_v = -(1 << 60)
        for r in range(n):
            row = rows[r]
            for c in range(m):
                if row[c] != STAR:
                    continue
                u, v = r + c, r - c
                lo_u = min(lo_u, u)
                hi_u = max(hi_u, u)
                lo_v = min(lo_v, v)
                hi_v = max(hi_v, v)
        if hi_u < lo_u:
            out.append("0")                 # nobody to hypnotise
            continue

        def worst(r, c):
            u, v = r + c, r - c
            return max(u - lo_u, hi_u - u, v - lo_v, hi_v - v)

        best = 1 << 60
        for r in range(n):
            # worst(r, .) is a max of linear functions, hence convex in c.
            left, right = 0, m - 1
            while right - left > 2:
                a = left + (right - left) // 3
                b = right - (right - left) // 3
                if worst(r, a) <= worst(r, b):
                    right = b
                else:
                    left = a
            for c in range(left, right + 1):
                best = min(best, worst(r, c))
        out.append(str(best + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
