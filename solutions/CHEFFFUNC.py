import sys


def solve(tokens):
    low, high = (next(tokens), next(tokens))
    best = 0
    for j in range(high.bit_length() + 1):
        candidate = low + (1 << j) - 1 >> j << j
        if candidate <= high:
            bits = candidate.bit_length()
            best = max(best, 3 * (1 << bits - 1) - 1 - candidate + bits - candidate.bit_count())
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
