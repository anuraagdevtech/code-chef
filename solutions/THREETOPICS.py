import sys


def main() -> None:
    # Single test case: one line of four integers, with no leading T.
    a, b, c, x = map(int, sys.stdin.buffer.read().split()[:4])
    print("Yes" if x in (a, b, c) else "No")


main()
