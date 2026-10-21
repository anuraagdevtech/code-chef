import sys

WIDTH = 32


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # Prefix counts per bit length: that is all the comparison depends on.
        pre = [[0] * (n + 1) for _ in range(WIDTH + 1)]
        for i in range(n):
            width = int(data[pos + 1 + i]).bit_length()
            for k in range(WIDTH + 1):
                pre[k][i + 1] = pre[k][i] + (k == width)
        pos += 1 + n
        q = int(data[pos])
        pos += 1
        for _ in range(q):
            l, r, x = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
            pos += 3
            same = pre[int(x).bit_length()]
            out.append(str((r - l + 1) - (same[r] - same[l - 1])))
    sys.stdout.write("\n".join(out) + "\n")


main()
