import sys


MOD = 998244353
fact = [1] * 200001
for i in range(1, 200001):
    fact[i] = fact[i - 1] * i % MOD
inv_fact = [1] * 200001
inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
for i in range(200000, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    mod = 998244353
    length = n + m - 1
    if length & 1:
        return '0'

    def comb(a, b):
        return fact[a] * inv_fact[b] % mod * inv_fact[a - b] % mod
    return str(comb(n + m - 2, n - 1) * comb(length, length // 2) % mod * pow(2, n * m - length, mod) % mod)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
