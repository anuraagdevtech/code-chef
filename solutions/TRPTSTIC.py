import sys
from array import array


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        m = next(tokens)
        people = next(tokens) + 1
        capacity = [next(tokens) for _ in range(n * m)]
        stride = m + 1
        prefix = array('q', [0]) * ((n + 1) * stride)
        for i in range(n):
            cur = 0
            row = (i + 1) * stride
            prev = i * stride
            for j in range(m):
                cur += capacity[i * m + j]
                prefix[row + j + 1] = prefix[prev + j + 1] + cur
        if prefix[-1] < people:
            out.append('-1')
            continue

        def possible(radius):
            for i in range(n):
                top = max(0, i - radius) * stride
                bot = min(n, i + radius + 1) * stride
                for j in range(m):
                    if capacity[i * m + j]:
                        l = max(0, j - radius)
                        r = min(m, j + radius + 1)
                        if prefix[bot + r] - prefix[top + r] - prefix[bot + l] + prefix[top + l] >= people:
                            return True
            return False
        low = 0
        high = max(n, m) - 1
        while low < high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        out.append(str(low))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
