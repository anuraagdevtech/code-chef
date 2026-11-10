"""Count ordered full binary trees by their leaf counts at each depth."""
import sys
from collections import Counter

MOD = 1000000007


def solve():
    it = iter(map(int,sys.stdin.buffer.read().split()))
    cases = []
    for _ in range(next(it)):
        n = next(it)
        cases.append([next(it) for _ in range(n)])
    limit = max(map(len,cases))
    fact = [1]*(limit+1)
    for i in range(1,limit+1):
        fact[i] = fact[i-1]*i % MOD
    inverse = [1]*(limit+1)
    inverse[-1] = pow(fact[-1],MOD-2,MOD)
    for i in range(limit,0,-1):
        inverse[i-1] = inverse[i]*i % MOD
    out = []
    for a in cases:
        counts = Counter(a)
        weight = sum(a)
        slots = 1
        remaining = len(a)
        answer = 1
        while remaining and slots:
            leaves = counts.get(weight,0)
            if leaves > slots or slots > remaining:
                answer = 0
                break
            answer = answer*fact[slots]*inverse[leaves]*inverse[slots-leaves] % MOD
            remaining -= leaves
            slots = 2*(slots-leaves)
            if slots and weight % 2:
                answer = 0
                break
            weight //= 2
        if remaining or slots:
            answer = 0
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    solve()
