import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        ring = [next(tokens) for _ in range(n)] * 2
        size = 2 * n
        prefix = [0]
        for value in ring:
            prefix.append(prefix[-1] + value)
        cost = [[0] * size for _ in range(size)]
        opt = [[0] * size for _ in range(size)]
        for i in range(size):
            opt[i][i] = i
        for length in range(2, n + 1):
            for i in range(size - length + 1):
                j = i + length - 1
                low = opt[i][j - 1]
                high = min(j - 1, opt[i + 1][j])
                best = 10 ** 30
                split = low
                for k in range(low, high + 1):
                    value = cost[i][k] + cost[k + 1][j]
                    if value < best:
                        best = value
                        split = k
                cost[i][j] = best + prefix[j + 1] - prefix[i]
                opt[i][j] = split
        out.append(str(min((cost[i][i + n - 1] for i in range(n)))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
