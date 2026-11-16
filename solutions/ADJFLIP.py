import sys


def solve(tokens):
    n = int(next(tokens))
    bits = next(tokens)
    balance = sum((1 if i % 2 == 0 else -1 for i, char in enumerate(bits) if char == 49))
    return 'Yes' if balance == 0 or (n % 2 and balance == 1) else 'No'


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
