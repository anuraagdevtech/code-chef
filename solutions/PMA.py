import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        total = 0
        min_plus = None       # smallest magnitude on an added position
        max_minus = None      # largest magnitude on a subtracted position
        for i, v in enumerate(vals):
            b = abs(int(v))
            if i % 2 == 0:
                total += b
                if min_plus is None or b < min_plus:
                    min_plus = b
            else:
                total -= b
                if max_minus is None or b > max_minus:
                    max_minus = b
        gain = 0
        if max_minus is not None:
            # The swap is optional, so never take a negative gain.
            gain = max(0, 2 * (max_minus - min_plus))
        out.append(str(total + gain))
    sys.stdout.write("\n".join(out) + "\n")


main()
