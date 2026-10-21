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
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = max(pre[i], a[i])
        suf = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            suf[i + 1] = max(suf[i + 2], a[i])
        # No operation can write a value above both neighbouring maxima.
        total = sum(max(a[i], min(pre[i], suf[i + 2])) for i in range(n))
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
