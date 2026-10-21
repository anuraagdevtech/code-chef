import sys

BITS = 30


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        # Each operation touches one bit position, so the columns are separate.
        counts = [0] * BITS
        for v in data[pos + 2:pos + 2 + n]:
            x = int(v)
            while x:
                low = x & -x
                counts[low.bit_length() - 1] += 1
                x ^= low
        pos += 2 + n
        out.append(str(sum((c + k - 1) // k for c in counts)))
    sys.stdout.write("\n".join(out) + "\n")


main()
