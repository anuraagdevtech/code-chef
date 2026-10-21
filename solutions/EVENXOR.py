import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # Doubling preserves the popcount, so the low bit repairs the parity.
        out.append(" ".join(str(2 * k + (k.bit_count() & 1))
                            for k in range(1, n + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
