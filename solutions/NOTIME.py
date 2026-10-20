import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    # Single test case: first line is N, H, x (not a test-case count).
    n, h, x = int(data[0]), int(data[1]), int(data[2])
    zones = data[3:3 + n]
    # Travelling back t hours leaves Chef with x + t; exactly enough counts.
    print("YES" if any(x + int(t) >= h for t in zones) else "NO")


main()
