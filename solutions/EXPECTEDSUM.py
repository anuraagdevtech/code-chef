import sys


def solve(tokens):
    a, b = (next(tokens), next(tokens))
    n = a + b
    MOD = 998244353
    return str(a * ((n + 1) // 2) * pow(n, MOD - 2, MOD) % MOD)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
