import sys


def solve(tokens):
    n = next(tokens)
    bits = [next(tokens) for _ in range(n)]
    best_at = {0: (1, 0)}
    previous = [-1] * (n + 1)
    height = 0
    best = (1, 0)
    for i, x in enumerate(bits, 1):
        height += 2 * x - 1
        v, j = best_at.get(height - 1, (0, -1))
        current = (v + 1, i)
        previous[i] = j
        if current[0] > best_at.get(height, (0, 0))[0]:
            best_at[height] = current
        if current[0] > best[0]:
            best = current
    chain = []
    j = best[1]
    while j >= 0:
        chain.append(j + 1)
        j = previous[j]
    return str(best[0]) + '\n' + ' '.join(map(str, reversed(chain)))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
