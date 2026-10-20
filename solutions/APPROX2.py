import sys
from collections import Counter


def count_sum(freq, s):
    """Unordered pairs of distinct positions whose values sum to s."""
    total = 0
    for v, c in freq.items():
        w = s - v
        if w not in freq:
            continue
        if v < w:
            total += c * freq[w]
        elif v == w:
            total += c * (c - 1) // 2      # two different positions
    return total


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        lo, hi = 0, n - 1
        best = abs(a[0] + a[1] - k)
        while lo < hi:
            s = a[lo] + a[hi]
            best = min(best, abs(s - k))
            if s < k:
                lo += 1
            else:
                hi -= 1
        freq = Counter(a)
        pairs = count_sum(freq, k - best)
        if best:                           # k - best and k + best coincide at 0
            pairs += count_sum(freq, k + best)
        out.append(f"{best} {pairs}")
    sys.stdout.write("\n".join(out) + "\n")


main()
