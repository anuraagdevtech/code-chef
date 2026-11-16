import sys
from collections import Counter


P = 1000000007
fact = [1] * 200001
for i in range(1, 200001):
    fact[i] = fact[i - 1] * i % P
inv_fact = [1] * 200001
inv_fact[-1] = pow(fact[-1], P - 2, P)
for i in range(200000, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % P


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    parent = list(range(n))
    size = [1] * n

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for _ in range(m):
        u, v = (root(next(tokens) - 1), root(next(tokens) - 1))
        if u != v:
            if size[u] < size[v]:
                u, v = (v, u)
            parent[v] = u
            size[u] += size[v]
    equal_groups = Counter(((root(i), next(tokens)) for i in range(n)))
    MOD = 1000000007
    answer = fact[n]
    for i in range(n):
        if parent[i] == i:
            answer = answer * inv_fact[size[i]] % MOD
    for count in equal_groups.values():
        answer = answer * fact[count] % MOD
    return str(answer)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
