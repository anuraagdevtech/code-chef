import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        prefix_min = [0] * n
        prefix_max = [0] * n
        low = high = values[0]
        prefix_min[0] = prefix_max[0] = values[0]
        for i in range(1, n):
            low = min(values[i], low + values[i])
            high = max(values[i], high + values[i])
            prefix_min[i] = min(prefix_min[i - 1], low)
            prefix_max[i] = max(prefix_max[i - 1], high)
        low = high = values[-1]
        suffix_min = suffix_max = values[-1]
        best = 0
        for i in range(n - 2, -1, -1):
            best = max(best, abs(prefix_max[i] - suffix_min), abs(prefix_min[i] - suffix_max))
            low = min(values[i], low + values[i])
            high = max(values[i], high + values[i])
            suffix_min = min(suffix_min, low)
            suffix_max = max(suffix_max, high)
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
