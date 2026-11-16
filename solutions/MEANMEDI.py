import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n, k = (next(tokens), next(tokens))
        values = sorted((next(tokens) for _ in range(n)))
        left_count = (k - 1) // 2
        right_count = k // 2
        dp = [1] + [0] * max(left_count, right_count)
        left = []
        for x in values:
            left.append(dp[left_count])
            for j in range(left_count, 0, -1):
                dp[j] |= dp[j - 1] << x
        dp = [1] + [0] * right_count
        right = [0] * n
        for i in range(n - 1, -1, -1):
            right[i] = dp[right_count]
            for j in range(right_count, 0, -1):
                dp[j] |= dp[j - 1] << values[i]
        best = 10 ** 9
        for i in range(left_count, n - right_count):
            left_sums = left[i]
            right_sums = right[i]
            target = values[i] * (k - 1)
            while left_sums:
                bit = left_sums & -left_sums
                s = bit.bit_length() - 1
                left_sums -= bit
                t = target - s
                if t < 0:
                    distance = s + (right_sums & -right_sums).bit_length() - 1 - target
                else:
                    lower = right_sums & (1 << t + 1) - 1
                    distance = abs(lower.bit_length() - 1 - t) if lower else 10 ** 9
                    upper = right_sums >> t
                    if upper:
                        distance = min(distance, (upper & -upper).bit_length() - 1)
                best = min(best, distance)
                if best == 0:
                    break
            if best == 0:
                break
        out.append('%.3f' % (best / k))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
