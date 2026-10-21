import sys

MOD = 10 ** 9 + 7


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        evens = sum(1 for v in data[pos + 1:pos + 1 + n] if int(v) % 2 == 0)
        pos += 1 + n
        # Every odd must go; each even is a free choice. The removal must be
        # non-empty, which only bites when there is nothing odd to remove.
        ways = pow(2, evens, MOD)
        if evens == n:
            ways -= 1
        out.append(str(ways % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
