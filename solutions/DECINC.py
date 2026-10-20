import sys


def main() -> None:
    # Single value, no test-case count on the first line.
    n = int(sys.stdin.buffer.read().split()[0])
    print(n + 1 if n % 4 == 0 else n - 1)


main()
