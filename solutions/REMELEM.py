import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        vals = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        if n == 1:
            out.append("YES")           # already a single element
        else:
            # The minimum is the best partner there is, so the maximum is the
            # binding case - not the second smallest.
            out.append("YES" if min(vals) + max(vals) <= k else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
