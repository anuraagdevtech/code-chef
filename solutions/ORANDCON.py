import sys

# X < 2^27, so these two bits are clear in X and act as distinct markers,
# while X | 2^28 still fits under 10^9.
MARK_B = 1 << 27
MARK_C = 1 << 28


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # The expression is a bitwise majority, so give all three every bit of
        # X and separate them with bits that only one of them holds.
        out.append(f"{x} {x | MARK_B} {x | MARK_C}")
    sys.stdout.write("\n".join(out) + "\n")


main()
