import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    cases = []
    largest = 0
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        odd = sum((next(tokens) % 2 for _ in range(n)))
        cases.append((n, k, odd))
        largest = max(largest, n)
    fact = [1] * (largest + 1)
    MOD = 10 ** 9 + 7
    for i in range(1, largest + 1):
        fact[i] = fact[i - 1] * i % MOD
    for n, k, odd_count in cases:
        if n == 1:
            answer = 1
        elif k == 0:
            answer = fact[n] if odd_count == 0 or odd_count == n else 0
        else:
            answer = fact[odd_count] * fact[n - odd_count] * ((odd_count == (n + 1) // 2) + (odd_count == n // 2)) % MOD
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
