import sys


def solve(tokens):
    n = next(tokens)
    weight = [next(tokens) for _ in range(n)]
    limit = [next(tokens) for _ in range(n)]
    left_need = [0] * (n + 1)
    right_need = [0] * (n + 1)
    for i in range(n):
        left_need[i + 1] = max(limit[i], left_need[i]) - weight[i]
    for i in range(n - 1, -1, -1):
        right_need[i] = max(limit[i], right_need[i + 1]) - weight[i]
    return ' '.join((str(max(limit[i], left_need[i] + right_need[i + 1]) - weight[i]) for i in range(n)))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
