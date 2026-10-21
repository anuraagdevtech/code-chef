import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted(int(x) for x in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # A product peaks at the extremes, so only the ends can matter.
        edge = sorted(set(list(range(min(3, n))) + list(range(max(0, n - 3), n))))
        best = None
        for i in edge:
            for j in edge:
                if i == j:
                    continue
                val = (a[i] - 1) * (a[j] + 1) + 1
                if best is None or val > best:
                    best = val
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
