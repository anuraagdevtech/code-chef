import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # AND never gains bits, so the best subarray through i is a pair.
        pairs = [a[i] & a[i + 1] for i in range(n - 1)]
        best = [0] * n
        best[0] = pairs[0]
        best[n - 1] = pairs[n - 2]
        for i in range(1, n - 1):
            best[i] = pairs[i - 1] if pairs[i - 1] > pairs[i] else pairs[i]
        out.append(" ".join(map(str, best)))
    sys.stdout.write("\n".join(out) + "\n")


main()
