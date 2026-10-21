import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        k = int(tok) - 1              # the list starts at 0
        digits = []
        # Magical numbers use digits {0,2,4,6,8}, so base 5 with doubled digits.
        while True:
            digits.append(str(2 * (k % 5)))
            k //= 5
            if not k:
                break
        out.append("".join(reversed(digits)))
    sys.stdout.write("\n".join(out) + "\n")


main()
