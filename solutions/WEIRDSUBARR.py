import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        p = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        inc = [1] * n
        dec = [1] * n
        for i in range(1, n):
            if p[i] > p[i - 1]:
                inc[i] = inc[i - 1] + 1
            if p[i] < p[i - 1]:
                dec[i] = dec[i - 1] + 1
        total = 0
        for r in range(n):
            # The turning point is forced to the start of r's increasing run.
            m = r - inc[r] + 1
            total += r - m + dec[m]
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
