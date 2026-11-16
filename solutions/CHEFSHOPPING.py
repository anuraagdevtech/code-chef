import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        left_cost = [next(tokens) for _ in range(n)]
        right_cost = [next(tokens) for _ in range(n)]
        out.append(str(sum((min(right_cost[i], left_cost[i + 1]) for i in range(n - 1)))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
