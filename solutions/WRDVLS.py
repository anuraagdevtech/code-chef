import sys


def solve(tokens):
    n = next(tokens)
    positions = {}
    for i in range(n):
        positions.setdefault(next(tokens), []).append(i)
    total = 0
    for value, occ in positions.items():
        if len(occ) < value:
            continue
        occ = [-1] + occ + [n]
        for j in range(1, len(occ) - value):
            total += value * (occ[j] - occ[j - 1]) * (occ[j + value] - occ[j + value - 1])
    return str(total)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
