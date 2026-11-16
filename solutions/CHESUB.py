import sys


def solve(tokens):
    n, k = (next(tokens), next(tokens))
    values = [next(tokens) for _ in range(n)]
    NEG = -10 ** 30
    best = [NEG] * (k + 1)
    end = best.copy()
    best[0] = 0
    for value in values:
        for j in range(k, 0, -1):
            end[j] = max(end[j], best[j - 1]) + j * value
            best[j] = max(best[j], end[j])
    return str(best[k])


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
