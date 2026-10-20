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
        # At most k originals can be overwritten, so the (k+1)-th smallest
        # survives. With k >= n - 1 the whole array can be flooded.
        out.append(str(a[min(k, n - 1)]))
    sys.stdout.write("\n".join(out) + "\n")


main()
