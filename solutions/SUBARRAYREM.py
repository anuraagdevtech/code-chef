import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        ones = sum(1 for v in data[pos + 1:pos + 1 + n] if v == b"1")
        pos += 1 + n
        zeros = n - ones
        # A zero-padded op costs one 1; without zeros an op needs three.
        cheap = min(ones, zeros)
        out.append(str(cheap + (ones - cheap) // 3))
    sys.stdout.write("\n".join(out) + "\n")


main()
