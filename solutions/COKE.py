import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, k, l, r = (int(v) for v in data[pos:pos + 5])
        pos += 5
        best = None
        for i in range(n):
            c, p = int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])
            gap = abs(c - k)
            # It snaps onto k once within one degree, so k is reached at m = gap.
            if m >= gap:
                final = k
            elif c > k:
                final = c - m
            else:
                final = c + m
            if l <= final <= r and (best is None or p < best):
                best = p
        pos += 2 * n
        out.append(str(best if best is not None else -1))
    sys.stdout.write("\n".join(out) + "\n")


main()
