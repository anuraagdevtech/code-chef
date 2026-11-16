import sys


def solve(tokens):
    n, k = (next(tokens), next(tokens))
    multiplier = pow(2, k, n - 1)
    return ' '.join((str(i * multiplier % (n - 1) + 1) for i in range(n - 1))) + ' ' + str(n)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
