import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        best = -1
        for v in data[pos + 2:pos + 2 + n]:
            p = int(v)
            # A player lands on the multiples of their own step size.
            # Larger divisors need fewer moves.
            if k % p == 0 and p > best:
                best = p
        pos += 2 + n
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
