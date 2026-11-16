import sys


def solve(tokens):
    n = next(tokens)
    piles = [next(tokens) for _ in range(n)]
    win = sum(piles) % 2 == 1 if n % 2 else min(piles) % 2 == 1 or sum(piles) % 2 == 1
    return 'CHEF' if win else 'CHEFINA'


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
