import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        coeffs = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        degree = 0
        for i, a in enumerate(coeffs):
            # The index is the exponent; negative coefficients still count.
            if int(a) != 0:
                degree = i
        out.append(str(degree))
    sys.stdout.write("\n".join(out) + "\n")


main()
