import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    b = [int(x) for x in data[1:1 + n]]
    levels = max(1, n.bit_length())
    lo, hi = [b[:]], [b[:]]
    step = 1
    while step * 2 <= n:
        prev_lo, prev_hi = lo[-1], hi[-1]
        lo.append([min(prev_lo[i], prev_lo[i + step])
                   for i in range(n - 2 * step + 1)])
        hi.append([max(prev_hi[i], prev_hi[i + step])
                   for i in range(n - 2 * step + 1)])
        step *= 2
    pre = [0] * (n + 1)              # max over b[0..i-1]
    for i in range(n):
        pre[i + 1] = max(pre[i], b[i])
    suf = [0] * (n + 2)              # max over b[i..n-1]
    for i in range(n - 1, -1, -1):
        suf[i] = max(suf[i + 1], b[i])

    pos = 1 + n
    q = int(data[pos])
    pos += 1
    out = []
    for _ in range(q):
        l, r = int(data[pos]), int(data[pos + 1])
        pos += 2
        k = (r - l + 1).bit_length() - 1
        shift = r - l + 1 - (1 << k)
        first = min(lo[k][l], lo[k][l + shift])
        worst_in = max(hi[k][l], hi[k][l + shift])
        best = (worst_in + first) / 2
        outside = max(pre[l], suf[r + 1])
        if outside:                  # unlit sticks only start at time `first`
            best = max(best, first + outside)
        out.append(f"{best:.1f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
