import sys

# Chef's code compares each element against all previous ones: 1 + 2 + ... +
# (n-1) = Theta(n^2) comparisons, so the exponent is 2.
COMPLEXITY_EXPONENT = 2


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])            # no test-case count
    # A hash set turns the O(i) membership scan into O(1) on average.
    print(COMPLEXITY_EXPONENT)
    print(len(set(data[1:1 + n])))


main()
