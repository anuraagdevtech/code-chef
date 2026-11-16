import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [(next(tokens), next(tokens), next(tokens)) for _ in range(next(tokens))]
    MOD = 1000000007
    most_balls = max((balls for runs, balls, wickets in cases), default=0)
    fact = [1] * (most_balls + 1)
    for i in range(1, most_balls + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (most_balls + 1)
    inv_fact[most_balls] = pow(fact[most_balls], MOD - 2, MOD)
    for i in range(most_balls, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    dot_ways = [[0] * 10 for _ in range(most_balls + 1)]
    for n in range(most_balls + 1):
        s = 0
        for wickets in range(10):
            if wickets <= n:
                s = (s + fact[n] * inv_fact[wickets] % MOD * inv_fact[n - wickets]) % MOD
            dot_ways[n][wickets] = s
    out = []
    for runs, balls, wickets in cases:
        total = 0
        if runs % 2 == 0 and runs <= 6 * balls:
            for six in range(min(balls, runs // 6) + 1):
                left = runs - 6 * six
                if left % 4:
                    continue
                four = left // 4
                n = balls - six - four
                if n >= 0:
                    total = (total + fact[balls] * inv_fact[six] % MOD * inv_fact[four] % MOD * inv_fact[n] % MOD * dot_ways[n][wickets]) % MOD
        out.append(str(total))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
