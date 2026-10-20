import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        best = 0
        prefix = 0
        for m in range(1, n + 1):
            prefix += a[m - 1]
            # The coupon saves floor(x / 2), so spend it on the dearest item
            # in the prefix - which, sorted, is the one just added.
            if prefix - a[m - 1] // 2 <= k:
                best = m
            else:
                break
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
