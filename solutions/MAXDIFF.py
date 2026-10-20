import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        w = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        total = sum(w)
        # The son's K items should be the lightest or the heaviest; which one
        # wins depends on K, so evaluate both.
        lightest, heaviest = sum(w[:k]), sum(w[n - k:])
        out.append(str(max(abs(total - 2 * lightest), abs(total - 2 * heaviest))))
    sys.stdout.write("\n".join(out) + "\n")


main()
