import sys


def solve(tokens):
    n, m, k = (next(tokens), next(tokens), next(tokens))
    sum_a = sum((next(tokens) for _ in range(n)))
    sum_b = sum((next(tokens) for _ in range(m)))
    if k == 1:
        return '-1'

    def ok(z):
        numerator = k * (m + z) - sum_a - sum_b - z + n
        denominator = 2 * (k - 1)
        x = numerator // denominator
        for t in (0, z, max(0, min(z, x)), max(0, min(z, x + 1))):
            if (sum_a + k * t) * (m + z - t) > (sum_b + z - t) * (n + t):
                return True
        return False
    low = -1
    high = 1
    while not ok(high):
        high *= 2
    while high - low > 1:
        mid = (high + low) // 2
        if ok(mid):
            high = mid
        else:
            low = mid
    return str(high)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
