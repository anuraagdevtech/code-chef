import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        s = bytearray(data[pos + 2])
        queries = data[pos + 3:pos + 3 + k]
        pos += 3 + k
        opposite = sum(s[i] != s[i + 1] for i in range(n - 1))
        base = 2 * (n - 1)
        for tok in queries:
            q = int(tok) - 1
            # Only q's own two pairs change, and both of them invert.
            for j in (q - 1, q):
                if 0 <= j < n - 1:
                    opposite -= s[j] != s[j + 1]
            s[q] ^= 1
            for j in (q - 1, q):
                if 0 <= j < n - 1:
                    opposite += s[j] != s[j + 1]
            out.append(str(base - opposite))
    sys.stdout.write("\n".join(out) + "\n")


main()
