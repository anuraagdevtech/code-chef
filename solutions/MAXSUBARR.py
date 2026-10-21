import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        m = int(data[pos + 1 + n])
        pos += 2 + n
        # Order inside the appended block never matters, only its sum.
        gain = sum(v for v in (int(x) for x in data[pos:pos + m]) if v > 0)
        pos += m

        best = run = 0
        for v in a:                       # Kadane, empty subarray allowed
            run = max(0, run + v)
            best = max(best, run)
        total = 0
        best_pre = 0
        for v in a:
            total += v
            best_pre = max(best_pre, total)
        best_suf = 0
        total = 0
        for v in reversed(a):
            total += v
            best_suf = max(best_suf, total)
        out.append(str(max(best, gain + best_pre, gain + best_suf)))
    sys.stdout.write("\n".join(out) + "\n")


main()
