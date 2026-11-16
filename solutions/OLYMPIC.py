import sys
from collections import Counter


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    village = [next(tokens) for _ in range(n)]
    queries = [next(tokens) for _ in range(next(tokens))]
    MOD = 1000000007
    chocolates = sum(village)
    fact = [1] * (chocolates + 1)
    for i in range(1, chocolates + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (chocolates + 1)
    inv_fact[chocolates] = pow(fact[chocolates], MOD - 2, MOD)
    for i in range(chocolates, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    events = {}
    total = chocolates
    denominator = half_denominator = 1
    odd = 0
    for value, multiplicity in Counter(village).items():
        denominator = denominator * pow(inv_fact[value], multiplicity, MOD) % MOD
        half_denominator = half_denominator * pow(inv_fact[value // 2], multiplicity, MOD) % MOD
        odd += value % 2 * multiplicity
        size = 1
        old = value
        while old > 1:
            end = (value - 1) // (old - 1)
            size = end + 1
            new = (value + size - 1) // size
            events.setdefault(size, []).append((old, new, multiplicity))
            old = new
    answers = {}
    keys = iter(sorted(events))
    nextsize = next(keys, None)
    for size in sorted(set(queries)):
        while nextsize is not None and nextsize <= size:
            for old, new, multiplicity in events[nextsize]:
                total += (new - old) * multiplicity
                odd += (new % 2 - old % 2) * multiplicity
                denominator = denominator * pow(fact[old] * inv_fact[new] % MOD, multiplicity, MOD) % MOD
                half_denominator = half_denominator * pow(fact[old // 2] * inv_fact[new // 2] % MOD, multiplicity, MOD) % MOD
            nextsize = next(keys, None)
        ways = fact[total] * denominator % MOD
        pal = fact[total // 2] * half_denominator % MOD if odd <= 1 else 0
        answers[size] = (ways + pal) * ((MOD + 1) // 2) % MOD
    print('\n'.join((str(answers[size]) for size in queries)))


if __name__ == "__main__":
    main()
