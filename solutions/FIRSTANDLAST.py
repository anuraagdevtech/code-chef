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
        # Rotating only slides the split point, so the ends are always a
        # cyclically adjacent pair. The wraparound pair must be included.
        best = max(a[i] + a[(i + 1) % n] for i in range(n))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
