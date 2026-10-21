import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        freq = [0] * (n + 2)
        for v in data[pos + 1:pos + 1 + n]:
            freq[int(v)] += 1
        pos += 1 + n
        # Elements of value <= t fit only in positions 1..t, which offer k*t
        # slots across k arrays.
        best = 1
        seen = 0
        for value in range(1, n + 1):
            seen += freq[value]
            need = (seen + value - 1) // value
            if need > best:
                best = need
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
