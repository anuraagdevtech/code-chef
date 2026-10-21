import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, q = int(data[pos]), int(data[pos + 1])
        pos += 2
        pre = [[0] * (n + 1) for _ in range(3)]
        for i in range(n):
            v = int(data[pos + i]) - 1
            for k in range(3):
                pre[k][i + 1] = pre[k][i] + (k == v)
        pos += n
        for _ in range(q):
            l, r = int(data[pos]), int(data[pos + 1])
            pos += 2
            m = r - l + 1
            # Even length, and one value must fill exactly one parity class.
            ok = m % 2 == 0 and any(
                pre[k][r] - pre[k][l - 1] == m // 2 for k in range(3))
            out.append("Yes" if ok else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
