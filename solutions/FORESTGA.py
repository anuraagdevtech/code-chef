import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    # Single test case: N, W, L then N pairs.
    n, w, l = int(data[0]), int(data[1]), int(data[2])
    trees = [(int(data[3 + 2 * i]), int(data[4 + 2 * i])) for i in range(n)]

    def harvest(months):
        total = 0
        for h, r in trees:
            height = h + r * months
            if height >= l:          # legality is per tree, not per total
                total += height
                if total >= w:       # early exit keeps the probe cheap
                    return total
        return total

    # Yield only ever grows, so binary search the first month that suffices.
    lo, hi = 0, 2 * 10 ** 18
    while lo < hi:
        mid = (lo + hi) // 2
        if harvest(mid) >= w:
            hi = mid
        else:
            lo = mid + 1
    print(lo)


main()
