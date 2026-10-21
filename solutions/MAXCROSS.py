import sys

CROSS = 0x58


def stamp(cells, best):
    """Mark every cell of each maximal run with that run's length."""
    k = len(cells)
    i = 0
    while i < k:
        j = i
        while j < k and cells[j] is not None:
            j += 1
        if j > i:
            length = j - i
            for p in range(i, j):
                if length > best[cells[p]]:
                    best[cells[p]] = length
            i = j
        else:
            i += 1


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    grid = data[1:1 + n]
    best = [0] * (n * n)
    mark = [[(r * n + c) if grid[r][c] == CROSS else None for c in range(n)]
            for r in range(n)]

    for r in range(n):
        stamp(mark[r], best)
    for c in range(n):
        stamp([mark[r][c] for r in range(n)], best)
    # Diagonals keep r - c constant; anti-diagonals keep r + c constant, and
    # the two indices run over different ranges.
    for d in range(-n + 1, n):
        stamp([mark[r][r - d] for r in range(max(0, d), min(n, n + d))], best)
    for d in range(2 * n - 1):
        stamp([mark[r][d - r] for r in range(max(0, d - n + 1), min(n, d + 1))], best)

    out = [" ".join(map(str, best[r * n:(r + 1) * n])) for r in range(n)]
    sys.stdout.write("\n".join(out) + "\n")


main()
