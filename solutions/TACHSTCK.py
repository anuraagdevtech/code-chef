import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    # No test-case count: first line is N and D.
    n, d = int(data[0]), int(data[1])
    lengths = sorted(int(v) for v in data[2:2 + n])
    pairs = 0
    i = 0
    while i + 1 < n:
        # Smallest remaining stick pairs with its nearest neighbour or not at all.
        if lengths[i + 1] - lengths[i] <= d:
            pairs += 1
            i += 2
        else:
            i += 1
    print(pairs)


main()
