import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n, m = (int(next(tokens)), int(next(tokens)))
    grid = [next(tokens) for _ in range(n)]
    below = [0] * (m + 1)
    total = 0
    for row in reversed(grid):
        current = [0] * (m + 1)
        run = 0
        for j in range(m - 1, -1, -1):
            run = run + 1 if row[j] == 49 else 0
            current[j] = min(run, below[j + 1] + 1)
            total += current[j]
        below = current
    print(total)


if __name__ == "__main__":
    main()
