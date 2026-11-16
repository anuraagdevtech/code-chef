import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        q = next(tokens)
        slope = [0] * (n + 2)
        intercept = [0] * (n + 2)
        for _ in range(q):
            left = next(tokens)
            right = next(tokens)
            slope[left] += 1
            slope[right + 1] -= 1
            intercept[left] += 1 - left
            intercept[right + 1] -= 1 - left
        active_slope = active_intercept = 0
        row = []
        for i in range(1, n + 1):
            active_slope += slope[i]
            active_intercept += intercept[i]
            row.append(str(active_slope * i + active_intercept))
        out.append(' '.join(row))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
