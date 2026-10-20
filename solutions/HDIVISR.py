import sys


def main() -> None:
    # Single integer, no test-case count.
    n = int(sys.stdin.buffer.read().split()[0])
    # Counting down means the first divisor found is the largest; d = 1 always
    # succeeds, so the search cannot come up empty.
    print(next(d for d in range(10, 0, -1) if n % d == 0))


main()
