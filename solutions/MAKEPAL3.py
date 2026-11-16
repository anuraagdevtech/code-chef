import sys


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    previous = moves = 0
    for i in range(n // 2):
        delta = values[i] - values[-1 - i]
        moves += abs(delta) if delta * previous < 0 else max(0, abs(delta) - abs(previous))
        previous = delta
    return str(moves)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
