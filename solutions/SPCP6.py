import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    queries = [next(tokens) for _ in range(next(tokens))]
    limit = max(queries)
    MOD = 10 ** 9 + 7
    chef = [0] * (limit + 1)
    chefina = [0] * (limit + 1)
    chef[0] = 1
    for i in range(1, limit + 1):
        chef[i] = (chefina[i - 1] + sum(chef[max(0, i - 4):max(0, i - 1)])) % MOD
        chefina[i] = (chef[i - 1] + sum(chefina[max(0, i - 4):max(0, i - 1)])) % MOD
    for lines in queries:
        out.append(str(sum(chef[max(0, lines - 4):lines]) % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
