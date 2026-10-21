import sys
from collections import deque


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, w = int(data[0]), int(data[1])
    h = [int(x) for x in data[2:2 + n]]
    hi, lo = deque(), deque()      # indices, values decreasing / increasing
    count = 0
    for i in range(n):
        while hi and h[hi[-1]] <= h[i]:
            hi.pop()
        hi.append(i)
        while lo and h[lo[-1]] >= h[i]:
            lo.pop()
        lo.append(i)
        left = i - w + 1
        if left < 0:
            continue
        if hi[0] < left:
            hi.popleft()
        if lo[0] < left:
            lo.popleft()
        # W distinct values span W - 1 only when they are consecutive.
        if h[hi[0]] - h[lo[0]] == w - 1:
            count += 1
    sys.stdout.write(f"{count}\n")


main()
