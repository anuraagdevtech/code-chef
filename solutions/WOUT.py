import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n, height = (next(tokens), next(tokens))
        row_gaps = [0] * (n + 1)
        for _ in range(n):
            low, high = (next(tokens), next(tokens))
            row_gaps[low] += 1
            row_gaps[high + 1] -= 1
        active = 0
        for i in range(n):
            active += row_gaps[i]
            row_gaps[i] = active
        window = sum(row_gaps[:height])
        best = window
        for i in range(height, n):
            window += row_gaps[i] - row_gaps[i - height]
            best = max(best, window)
        out.append(str(n * height - best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
