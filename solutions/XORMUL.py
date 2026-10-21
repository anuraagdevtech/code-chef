import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 3 * i])
        a, b = int(data[2 + 3 * i]), int(data[3 + 3 * i])
        diff = a ^ b
        # Agreeing bits: flip them up so both factors gain them.
        x = ((1 << n) - 1) ^ diff ^ (a & ~diff)
        if diff:
            top = 1 << (diff.bit_length() - 1)
            # Top differing bit to one factor, all the lower ones to the other.
            x |= (~a & top) | (~b & diff & ~top)
            x &= (1 << n) - 1
        out.append(str(x))
    sys.stdout.write("\n".join(out) + "\n")


main()
