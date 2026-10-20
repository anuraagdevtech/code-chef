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
        if n % 2:
            out.append("-1")          # an odd count can never sum to zero
            continue
        plus = sum(1 for v in vals if v == b"1")
        # Each flip moves the +1 count by exactly one.
        out.append(str(abs(plus - n // 2)))
    sys.stdout.write("\n".join(out) + "\n")


main()
