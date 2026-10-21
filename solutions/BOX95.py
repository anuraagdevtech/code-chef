import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        top = 1 << (max(vals).bit_length() - 1)
        # Each box holds at most two elements carrying the top bit, and the
        # guarantee 2*XOR >= OR forces their count to be odd.
        k = sum(1 for v in vals if v & top)
        out.append(str((k + 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
