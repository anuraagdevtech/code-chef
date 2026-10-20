import sys

# Ranked by how common the colour is: brown > blue > green.
RANK = {"R": 2, "B": 1, "G": 0}


def main() -> None:
    # Single test case: two space-separated characters.
    a, b = sys.stdin.buffer.read().split()[:2]
    print(max(a.decode(), b.decode(), key=lambda c: RANK[c]))


main()
