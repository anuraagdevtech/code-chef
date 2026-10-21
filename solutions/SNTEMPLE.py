import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        h = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Tallest slope that can end here, capped by the block's own height
        # because blocks may only be reduced.
        left = [0] * n
        left[0] = min(h[0], 1)
        for i in range(1, n):
            left[i] = min(h[i], left[i - 1] + 1)
        right = [0] * n
        right[n - 1] = min(h[n - 1], 1)
        for i in range(n - 2, -1, -1):
            right[i] = min(h[i], right[i + 1] + 1)
        peak = max(min(left[i], right[i]) for i in range(n))
        out.append(str(sum(h) - peak * peak))
    sys.stdout.write("\n".join(out) + "\n")


main()
