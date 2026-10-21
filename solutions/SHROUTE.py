import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        a = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # Nearest right-mover at or before i, and left-mover at or after i.
        prev_right = [-1] * (n + 1)
        last = -1
        for i in range(1, n + 1):
            if a[i - 1] == b"1":
                last = i
            prev_right[i] = last
        next_left = [-1] * (n + 2)
        nxt = -1
        for i in range(n, 0, -1):
            if a[i - 1] == b"2":
                nxt = i
            next_left[i] = nxt
        res = []
        for i in range(m):
            b = int(data[pos + i])
            best = -1
            if prev_right[b] != -1:
                best = b - prev_right[b]
            if next_left[b] != -1:
                cand = next_left[b] - b
                best = cand if best == -1 else min(best, cand)
            res.append(str(best))
        pos += m
        out.append(" ".join(res))
    sys.stdout.write("\n".join(out) + "\n")


main()
