import sys


def solve(tokens):
    int(next(tokens))
    text = next(tokens)
    MOD = 1000000007
    strings = 1
    count_4 = count_40 = count_404 = 0
    for char in text:
        if char == 52:
            count_4 = (count_4 + strings) % MOD
            count_404 = (count_404 + count_40) % MOD
        elif char == 48:
            count_40 = (count_40 + count_4) % MOD
        else:
            strings, count_4, count_40, count_404 = (2 * strings % MOD, (2 * count_4 + strings) % MOD, (2 * count_40 + count_4) % MOD, (2 * count_404 + count_40) % MOD)
    return str(count_404)


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
