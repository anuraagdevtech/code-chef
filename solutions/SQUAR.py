import sys
from array import array
from collections import Counter


raw = list(map(int, sys.stdin.buffer.read().split()))
V = max(raw)
spf = array('I', [0]) * (V + 1)
for i in range(2, int(V ** 0.5) + 1):
    if not spf[i]:
        for j in range(i * i, V + 1, i):
            if not spf[j]:
                spf[j] = i


def solve(tokens):
    n = next(tokens)
    count = Counter()
    for _ in range(n):
        value = next(tokens)
        kernel = 1
        while value > 1:
            prime = spf[value] or value
            odd = 0
            while value % prime == 0:
                value //= prime
                odd ^= 1
            if odd:
                kernel *= prime
        if kernel != 1:
            count[kernel] += 1
    return str(max(count.values(), default=0))


if __name__ == "__main__":
    tokens = iter(raw)
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
