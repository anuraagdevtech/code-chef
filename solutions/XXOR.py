import sys

BITS = 31


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    a = [int(x) for x in data[2:2 + n]]
    # pref[b][i] = how many of the first i elements have bit b set.
    pref = []
    for b in range(BITS):
        run = [0] * (n + 1)
        mask = 1 << b
        total = 0
        for i, v in enumerate(a):
            if v & mask:
                total += 1
            run[i + 1] = total
        pref.append(run)

    out = []
    pos = 2 + n
    for _ in range(q):
        l, r = int(data[pos]), int(data[pos + 1])
        pos += 2
        m = r - l + 1
        x = 0
        for b in range(BITS):
            run = pref[b]
            ones = run[r] - run[l - 1]
            # Flip only when it strictly helps; a tie keeps the bit 0 so that
            # X stays as small as possible.
            if 2 * ones < m:
                x |= 1 << b
        out.append(str(x))
    sys.stdout.write("\n".join(out) + "\n")


main()
