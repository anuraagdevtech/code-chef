import sys


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    counts = [0] * 30
    for _ in range(n):
        x = next(tokens)
        while x:
            v = x & -x
            counts[v.bit_length() - 1] += 1
            x -= v
    MOD = 998244353
    inverse = [0, 1] + [0] * (n - 1)
    for k in range(2, n + 1):
        inverse[k] = MOD - MOD // k * inverse[MOD % k] % MOD
    binom = [1] * (n + 1)
    for k in range(1, n + 1):
        binom[k] = binom[k - 1] * (n - k + 1) % MOD * inverse[k] % MOD
    groups = {}
    for b, count in enumerate(counts):
        if count:
            groups[count] = (groups.get(count, 0) + (1 << b)) % MOD
    answers = [0] * (n + 1)
    half = (MOD + 1) // 2
    for count, weight in groups.items():
        drift = n - 2 * count
        previous = 1
        current = drift % MOD
        weight = weight * half % MOD
        for k in range(1, n + 1):
            answers[k] = (answers[k] + weight * (binom[k] - current)) % MOD
            previous, current = (current, (drift * current - (n - k + 1) * previous) * inverse[k + 1] % MOD if k < n else 0)
    for k in range(1, n + 1):
        answers[k] = (answers[k] + answers[k - 1]) % MOD
    q = next(tokens)
    print('\n'.join((str(answers[next(tokens)]) for _ in range(q))))


if __name__ == "__main__":
    main()
