import sys


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    parent = list(range(n))
    size = [1] * n
    components = n
    total = 0

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for bit in range(30):
        first = -1
        for i, x in enumerate(values):
            if x >> bit & 1:
                if first < 0:
                    first = i
                    continue
                u, v = (root(first), root(i))
                if u != v:
                    if size[u] < size[v]:
                        u, v = (v, u)
                    parent[v] = u
                    size[u] += size[v]
                    components -= 1
                    total += 1 << bit
    return str(total if components == 1 else -1)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
