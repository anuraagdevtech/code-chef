import sys

INF = float("inf")
CLEAN = 0x2E       # '.'


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        top, bot = data[1 + 2 * i], data[2 + 2 * i]
        n = len(top)
        a = 0 if top[0] == CLEAN else INF
        b = 0 if bot[0] == CLEAN else INF
        for x in range(n):
            if x:
                prev_a, prev_b = a, b
                # Arrive by advancing (free) or by switching lanes (cost 1).
                a = min(prev_a, prev_b + 1) if top[x] == CLEAN else INF
                b = min(prev_b, prev_a + 1) if bot[x] == CLEAN else INF
            # A switch inside the column; once each way is enough.
            if top[x] == CLEAN and b + 1 < a:
                a = b + 1
            if bot[x] == CLEAN and a + 1 < b:
                b = a + 1
        best = a if a < b else b
        out.append("No" if best == INF else f"Yes\n{best}")
    sys.stdout.write("\n".join(out) + "\n")


main()
