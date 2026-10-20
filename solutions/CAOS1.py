import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        rows, cols = int(data[pos]), int(data[pos + 1])
        grid = [data[pos + 2 + i].decode() for i in range(rows)]
        pos += 2 + rows
        open_ = [[c == "^" for c in row] for row in grid]
        left = [[0] * cols for _ in range(rows)]
        right = [[0] * cols for _ in range(rows)]
        top = [[0] * cols for _ in range(rows)]
        bottom = [[0] * cols for _ in range(rows)]
        # Each run is the neighbour's run plus one, or zero at a wall.
        for r in range(rows):
            for c in range(1, cols):
                left[r][c] = left[r][c - 1] + 1 if open_[r][c - 1] else 0
            for c in range(cols - 2, -1, -1):
                right[r][c] = right[r][c + 1] + 1 if open_[r][c + 1] else 0
        for c in range(cols):
            for r in range(1, rows):
                top[r][c] = top[r - 1][c] + 1 if open_[r - 1][c] else 0
            for r in range(rows - 2, -1, -1):
                bottom[r][c] = bottom[r + 1][c] + 1 if open_[r + 1][c] else 0
        # The smallest prime is 2, so "some prime <= min" means min >= 2.
        count = sum(1 for r in range(rows) for c in range(cols)
                    if open_[r][c]
                    and min(left[r][c], right[r][c], top[r][c], bottom[r][c]) >= 2)
        out.append(str(count))
    sys.stdout.write("\n".join(out) + "\n")


main()
