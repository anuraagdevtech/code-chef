import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        others = [v for v in vals if v > 1]
        ones = n - len(others)
        if not others:
            out.append(str(ones % MOD))       # nothing is worth multiplying
            continue
        if ones >= 2:
            seed = ones                       # add every one, multiply the rest
        else:
            # With no ones, a * (product / a) is the full product either way;
            # with exactly one, adding the smallest factor too beats keeping it.
            smallest = min(others)
            others.remove(smallest)
            seed = ones + smallest
        prod = 1
        for v in others:
            prod = prod * v % MOD
        out.append(str(seed * prod % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
