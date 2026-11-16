import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    MOD = 1000000007
    for _ in range(next(tokens)):
        n, m = (next(tokens), next(tokens))
        commands = [(next(tokens), next(tokens) - 1, next(tokens) - 1) for _ in range(m)]
        delta = [0] * (m + 1)
        diff = [0] * (n + 1)
        extra = 0
        for i in range(m - 1, -1, -1):
            extra = (extra + delta[i]) % MOD
            count = extra + 1
            kind, left, right = commands[i]
            if kind == 2:
                delta[right] = (delta[right] + count) % MOD
                delta[left - 1 if left else m] = (delta[left - 1 if left else m] - count) % MOD
            else:
                diff[left] += count
                diff[right + 1] -= count
        total = 0
        row = []
        for x in diff[:n]:
            total = (total + x) % MOD
            row.append(str(total))
        out.append(' '.join(row))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
