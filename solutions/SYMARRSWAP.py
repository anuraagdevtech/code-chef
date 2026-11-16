import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        first = [next(tokens) for _ in range(n)]
        second = [next(tokens) for _ in range(n)]
        items = sorted([(value, i) for i, value in enumerate(first)] + [(value, i) for i, value in enumerate(second)])
        counts = [0] * n
        have = 0
        left = 0
        best = 10 ** 18
        for r, (value, i) in enumerate(items):
            if counts[i] == 0:
                have += 1
            counts[i] += 1
            while have == n:
                best = min(best, value - items[left][0])
                j = items[left][1]
                counts[j] -= 1
                left += 1
                if counts[j] == 0:
                    have -= 1
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
