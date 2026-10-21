import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, q = int(data[pos]), int(data[pos + 1])
        a = [int(x) for x in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        # gcd(0, x) == x makes 0 the identity, so the ends need no special case.
        pre = [0] * (n + 2)
        for i in range(n):
            pre[i + 1] = gcd(pre[i], a[i])
        suf = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            suf[i + 1] = gcd(suf[i + 2], a[i])
        for _ in range(q):
            l, r = int(data[pos]), int(data[pos + 1])
            pos += 2
            out.append(str(gcd(pre[l - 1], suf[r + 1])))
    sys.stdout.write("\n".join(out) + "\n")


main()
