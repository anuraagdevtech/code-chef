import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])                 # no test-case count
    a = [int(v) for v in data[1:1 + n]]
    swaps = []
    # Insertion sort only swaps genuine inversions, so it hits the minimum.
    # Its real cost is O(n + inversions), not O(n^2).
    for i in range(1, n):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            swaps.append(j - 1)
            j -= 1
    sys.stdout.write(f"{len(swaps)}\n" + " ".join(map(str, swaps)) + "\n")


main()
