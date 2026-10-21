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
        # An optimal choice is contiguous once sorted, so slide a window.
        out.append(str(min(a[i + k - 1] - a[i] for i in range(n - k + 1))))
    sys.stdout.write("\n".join(out) + "\n")


main()
