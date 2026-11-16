import sys
from collections import Counter


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    prefix = [0]
    for value in values + values:
        prefix.append(prefix[-1] ^ value)
    window = Counter(prefix[1:n + 1])
    best = len(window)
    for i in range(1, n):
        value = prefix[i]
        window[value] -= 1
        if not window[value]:
            del window[value]
        value = prefix[i + n]
        window[value] += 1
        best = max(best, len(window))
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
