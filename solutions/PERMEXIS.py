import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # If sorting cannot do it, no arrangement can: a gap > 1 splits the
        # values into two groups that no ordering can bridge.
        ok = all(a[i + 1] - a[i] <= 1 for i in range(n - 1))
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
