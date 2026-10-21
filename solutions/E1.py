import sys

NEG = -1
PAWN = 0x50


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        board = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        start = next(r for r in range(n) if board[r].find(b"K") >= 0)
        # Rolling window: a column only ever feeds the next two.
        cur = [NEG] * n
        nxt1 = [NEG] * n
        nxt2 = [NEG] * n
        cur[start] = 0
        best = NEG
        for c in range(n):
            if c == n - 1:
                best = max(cur)
                break
            for r in range(n):
                here = cur[r]
                if here < 0:
                    continue
                for dr in (-2, 2):                 # column + 1
                    rr = r + dr
                    if 0 <= rr < n:
                        gain = here + (board[rr][c + 1] == PAWN)
                        if gain > nxt1[rr]:
                            nxt1[rr] = gain
                if c + 2 < n:
                    for dr in (-1, 1):             # column + 2
                        rr = r + dr
                        if 0 <= rr < n:
                            gain = here + (board[rr][c + 2] == PAWN)
                            if gain > nxt2[rr]:
                                nxt2[rr] = gain
            cur, nxt1, nxt2 = nxt1, nxt2, [NEG] * n
        out.append(str(max(best, 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
