import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 3 * i]), int(data[2 + 3 * i])
        a = data[3 + 3 * i]
        ones = a.count(0x31)
        if ones == 0:
            out.append(str(n * m))        # every prefix sum is already 0
            continue
        if (m * ones) % 2:
            out.append("0")               # the total cannot be halved
            continue
        seen = Counter()
        run = 0
        for c in a:
            run += c == 0x31
            seen[run] += 1
        half = m * ones // 2
        # Only the copy around H / S can host a matching prefix.
        base = half // ones
        total = 0
        for j in (base - 1, base):
            if 0 <= j < m:
                total += seen.get(half - j * ones, 0)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
