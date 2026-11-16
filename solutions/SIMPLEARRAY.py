import sys


def solve(tokens):
    n, k = (next(tokens), next(tokens))
    count = [0] * k
    for _ in range(n):
        count[next(tokens) % k] += 1
    MOD = 1000000007
    answer = count[0] + 1
    for residue in range(1, (k + 1) // 2):
        answer = answer * (pow(2, count[residue], MOD) + pow(2, count[k - residue], MOD) - 1) % MOD
    if k % 2 == 0:
        answer = answer * (count[k // 2] + 1) % MOD
    return str(answer)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
