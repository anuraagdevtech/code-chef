import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [(next(tokens), next(tokens), next(tokens), next(tokens)) for _ in range(next(tokens))]
    MOD = 1000000007
    limit = max((n + m for n, m, a, b in cases), default=0)
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (limit + 1)
    inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def choose(n, k):
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    out = []
    for n, m, a, b in cases:
        answer = 0
        for x in range(n - a + 1):
            answer = (answer + choose(x + b - 1, x) * choose(n - x + m - b, n - x)) % MOD
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
