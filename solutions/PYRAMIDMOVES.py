import sys
from math import isqrt


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    cases = [(next(tokens), next(tokens)) for _ in range(next(tokens))]
    MOD = 10 ** 9 + 7
    LIMIT = 50000
    fact = [1] * (LIMIT + 1)
    for i in range(1, LIMIT + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (LIMIT + 1)
    inv_fact[LIMIT] = pow(fact[LIMIT], -1, MOD)
    for i in range(LIMIT, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def cell(x):
        r = (isqrt(8 * x - 7) + 1) // 2
        if r * (r + 1) // 2 < x:
            r += 1
        return (r, x - r * (r - 1) // 2)
    for start, end in cases:
        r, c = cell(start)
        u, v = cell(end)
        down = u - r
        right = v - c
        out.append(str(fact[down] * inv_fact[right] % MOD * inv_fact[down - right] % MOD) if 0 <= right <= down else '0')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
