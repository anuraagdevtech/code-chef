import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        big_d, d, p, q = map(int, data[1 + 4 * i:5 + 4 * i])
        full, rem = divmod(big_d, d)
        # Complete blocks form an arithmetic series; the leftover days run at
        # the next rate up.
        total = d * (full * p + q * full * (full - 1) // 2)
        total += rem * (p + full * q)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
