import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted(int(x) for x in data[pos + 1:pos + 1 + 2 * n])
        pos += 1 + 2 * n
        k = (n + 1) // 2
        out.append(str(a[2 * n - k]))
        # Each of the k largest carries its own pair, partnered by a smallest.
        order = []
        for j in range(k):
            order.append(a[j])
            order.append(a[2 * n - k + j])
        order.extend(a[k:2 * n - k])
        out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


main()
