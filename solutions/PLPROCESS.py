import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        total = sum(a)
        # Both split extremes are legal, so start from an empty prefix.
        best = total
        prefix = 0
        for v in a:
            prefix += v
            # They run at the same time, so the cost is the heavier side.
            best = min(best, max(prefix, total - prefix))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
