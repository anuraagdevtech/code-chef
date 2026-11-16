import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [(next(tokens), next(tokens), next(tokens)) for _ in range(next(tokens))]
    MOD = 1000000007
    most_days = max((n for n, m, k in cases), default=0)
    by_days = {}
    for i, c in enumerate(cases):
        by_days.setdefault(c[0], []).append((i, c[1], c[2]))
    stirling = [1] + [0] * most_days
    answers = [0] * len(cases)
    for n in range(1, most_days + 1):
        for j in range(n, 0, -1):
            stirling[j] = (stirling[j] * j + stirling[j - 1]) % MOD
        stirling[0] = 0
        for i, m, k in by_days.get(n, []):
            fall = 1
            total = 0
            for j in range(1, min(n, m, k) + 1):
                fall = fall * (m - j + 1) % MOD
                total = (total + fall * stirling[j]) % MOD
            answers[i] = total
    print('\n'.join(map(str, answers)))


if __name__ == "__main__":
    main()
