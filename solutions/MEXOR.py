import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        x = int(tok)
        # OR(0..m-1) is 2^bitlen(m-1) - 1, so the answer is a power of two.
        out.append(str(1 << ((x + 1).bit_length() - 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
