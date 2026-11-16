import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    MOD = 10 ** 9 + 7
    mx = 100000
    fact = [1] * (mx + 1)
    inv_fact = [1] * (mx + 1)
    pow2 = [1] * (mx + 1)
    inv_pow2 = [1] * (mx + 1)
    half = (MOD + 1) // 2
    for i in range(1, mx + 1):
        fact[i] = fact[i - 1] * i % MOD
        pow2[i] = pow2[i - 1] * 2 % MOD
        inv_pow2[i] = inv_pow2[i - 1] * half % MOD
    inv_fact[mx] = pow(fact[mx], -1, MOD)
    for i in range(mx, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def choose(n, k):
        return 0 if k < 0 or k > n else fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    for _ in range(next(tokens)):
        n = next(tokens)
        counts = [0] * (n + 1)
        for _ in range(n):
            counts[next(tokens)] += 1
        size = 0
        tail = 0
        total = 0
        for v in range(1, n + 1):
            old = tail
            for _ in range(counts[v]):
                tail = (tail + choose(size, v - 1) * inv_pow2[size + 1]) % MOD
                size += 1
            total = (total + tail - old) % MOD
            tail = (tail - choose(size, v) * inv_pow2[size]) % MOD
        out.append(str(total * pow2[n] % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
