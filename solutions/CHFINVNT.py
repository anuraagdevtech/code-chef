import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, p, k = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        r = p % k
        full, tail = n // k, n % k
        # Each full block of K holds r small residues; the short tail may not.
        earlier = full * r + (r if r < tail else tail)
        out.append(str(earlier + p // k + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
