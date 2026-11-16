import sys


def solve(tokens):
    bits = next(tokens)
    n = len(bits)
    total = best = running = 0
    for i, char in enumerate(bits, 1):
        weight = i * (n - i + 1)
        if char == 49:
            total += weight
            weight = -weight
        running = max(0, running + weight)
        best = max(best, running)
    return str(total + best)


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
