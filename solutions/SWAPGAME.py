import sys


def solve(tokens):
    n = next(tokens)
    source = [next(tokens) for _ in range(n)]
    target = [next(tokens) for _ in range(n)]
    return str(sum((i * (y - x) for i, (x, y) in enumerate(zip(source, target)))))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
