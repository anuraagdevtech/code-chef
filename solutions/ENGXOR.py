import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, q = int(data[pos]), int(data[pos + 1])
        pos += 2
        odd = 0
        for tok in data[pos:pos + n]:
            odd += int(tok).bit_count() & 1
        pos += n
        even = n - odd
        for tok in data[pos:pos + q]:
            # XOR adds the two popcounts mod 2, so odd P just swaps the tallies.
            if int(tok).bit_count() & 1:
                out.append(f"{odd} {even}")
            else:
                out.append(f"{even} {odd}")
        pos += q
    sys.stdout.write("\n".join(out) + "\n")


main()
