import sys

BITS = 10          # A_i <= 1000 < 2^10


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        pos += 2
        basis = [0] * BITS          # basis[b] has its highest set bit at b
        for tok in data[pos:pos + n]:
            v = int(tok)
            for b in range(BITS - 1, -1, -1):
                if not v >> b & 1:
                    continue
                if not basis[b]:
                    basis[b] = v
                    break
                v ^= basis[b]       # cancel and keep reducing
        pos += n
        res = k
        for b in range(BITS - 1, -1, -1):
            # 2^b outweighs every lower bit, so take the bit whenever we can.
            if basis[b] and not res >> b & 1:
                res ^= basis[b]
        out.append(str(res))
    sys.stdout.write("\n".join(out) + "\n")


main()
