import sys


def main() -> None:
    # Single test case: one line with X and Y, no leading T.
    x, y = map(int, sys.stdin.buffer.read().split()[:2])
    # y minutes of footage at 2x costs y // 2 minutes of real time.
    print(y // 2 + (x - y))


main()
