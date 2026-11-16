import sys


def solve(tokens):
    n, limit = (next(tokens), next(tokens))
    perm = [next(tokens) - 1 for _ in range(n)]
    values = [next(tokens) for _ in range(n)]
    source = list(range(n))
    for i in range(n):
        source[i] = source[perm[i]]
    used = set(source)
    fixed = {values[i] for i in used if values[i]}
    free = sum((values[i] == 0 for i in range(n) if i not in used))
    return str(0 if len(fixed) > 1 else pow(limit, free + (not fixed), 1000000007))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
