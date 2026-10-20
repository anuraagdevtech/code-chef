import sys


def main() -> None:
    # Single test case; input order is R, O, C.
    r, o, c = map(int, sys.stdin.buffer.read().split()[:3])
    # Best case: 6 balls x 6 runs = 36 per over, for the overs that remain.
    best = c + 36 * (20 - o)
    print("YES" if best > r else "NO")


main()
