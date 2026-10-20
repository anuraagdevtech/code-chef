import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # A zero makes the product 0, which beats any parity concern.
        if any(v == 0 for v in vals):
            out.append("0")
        else:
            negatives = sum(1 for v in vals if v < 0)
            out.append("0" if negatives % 2 == 0 else "1")
    sys.stdout.write("\n".join(out) + "\n")


main()
