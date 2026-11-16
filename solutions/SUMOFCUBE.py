import sys


def solve(tokens):
    n = next(tokens)
    MOD = 998244353
    prefix = s1 = s2 = s3 = total = 0
    for i in range(1, n + 1):
        prefix = (prefix + next(tokens)) % MOD
        p2 = prefix * prefix % MOD
        p3 = p2 * prefix % MOD
        total = (total + i * p3 - 3 * p2 * s1 + 3 * prefix * s2 - s3) % MOD
        s1 = (s1 + prefix) % MOD
        s2 = (s2 + p2) % MOD
        s3 = (s3 + p3) % MOD
    return str(total)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
