import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = sorted(int(x) for x in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # a_i tops 2^i subsets and bottoms 2^(n-1-i) of them.
        total = 0
        low, high = 1, pow(2, n - 1, MOD)
        inv2 = (MOD + 1) // 2
        for v in vals:
            total = (total + v * (low - high)) % MOD
            low = low * 2 % MOD
            high = high * inv2 % MOD
        out.append(str(total % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
