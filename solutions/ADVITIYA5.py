import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        odds = list(range(1, n + 1, 2))
        evens = list(range(2, n + 1, 2))
        blocks = k + 1                       # b blocks give b - 1 changes
        o_blocks, e_blocks = (blocks + 1) // 2, blocks // 2
        # Surplus goes into the first block of each parity: padding a block
        # never adds a change.
        res = []
        oi = ei = 0
        for b in range(blocks):
            if b % 2 == 0:
                take = len(odds) - o_blocks + 1 if b == 0 else 1
                res.extend(odds[oi:oi + take])
                oi += take
            else:
                take = len(evens) - e_blocks + 1 if b == 1 else 1
                res.extend(evens[ei:ei + take])
                ei += take
        out.append(" ".join(map(str, res)))
    sys.stdout.write("\n".join(out) + "\n")


main()
