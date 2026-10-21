import sys

LAND = 0x31


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        rows = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        grid = bytearray(n * m)
        for r in range(n):
            base = r * m
            row = rows[r]
            for c in range(m):
                if row[c] == LAND:
                    grid[base + c] = 1
        sizes = []
        for start in range(n * m):
            if not grid[start]:
                continue
            grid[start] = 0
            stack = [start]
            size = 0
            while stack:                      # explicit stack, no recursion
                cell = stack.pop()
                size += 1
                r, c = divmod(cell, m)
                if c and grid[cell - 1]:
                    grid[cell - 1] = 0
                    stack.append(cell - 1)
                if c + 1 < m and grid[cell + 1]:
                    grid[cell + 1] = 0
                    stack.append(cell + 1)
                if r and grid[cell - m]:
                    grid[cell - m] = 0
                    stack.append(cell - m)
                if r + 1 < n and grid[cell + m]:
                    grid[cell + m] = 0
                    stack.append(cell + m)
            sizes.append(size)
        sizes.sort(reverse=True)
        # Both players take the largest left, so Mike gets the odd positions.
        out.append(str(sum(sizes[1::2])))
    sys.stdout.write("\n".join(out) + "\n")


main()
