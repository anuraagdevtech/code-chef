import sys


def digit_sum(x: int) -> int:
    return sum(map(int, str(x)))


def main() -> None:
    # Single value, no test-case count.
    n = int(sys.stdin.buffer.read().split()[0])
    # S(X) <= 90 and S(S(X)) <= 18 for X <= 1e9, so X cannot be far below N.
    count = 0
    for x in range(max(1, n - 200), n + 1):
        if x + digit_sum(x) + digit_sum(digit_sum(x)) == n:
            count += 1
    print(count)


main()
