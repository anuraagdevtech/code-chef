import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted((int(x) for x in data[pos + 1:pos + 1 + n]), reverse=True)
        pos += 1 + n
        total = sum(a)
        best = 0
        attack = 0
        for k in range(n + 1):
            if k:
                attack += a[k - 1]
            # The remaining soldiers defend, each worth 1000 - A_i.
            defend = 1000 * (n - k) - (total - attack)
            best = max(best, attack * defend)
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
