import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    n = next(tokens)
    remainder = next(tokens)
    values = [next(tokens) for _ in range(n)]
    limit = max(values)
    divisors = [[] for _ in range(max(1, limit - remainder + 1))]
    for divisor in range(remainder + 1, limit - remainder + 1):
        for v in range(divisor, limit - remainder + 1, divisor):
            divisors[v].append(divisor)
    last = [-1] * (limit + 1)
    special = -1
    left = 0
    total = 0
    for i, value in enumerate(values):
        if value > remainder:
            left = max(left, last[value] + 1, special + 1)
        total += i - left + 1
        if value == remainder:
            special = i
        elif value > remainder:
            for divisor in divisors[value - remainder]:
                last[divisor] = i
    print(total)


if __name__ == "__main__":
    main()
