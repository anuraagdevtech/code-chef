import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        pos += 2
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for _ in range(m):
            a, b = find(int(data[pos])), find(int(data[pos + 1]))
            pos += 2
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
        routes = 0
        ways = 1
        for v in range(1, n + 1):
            if find(v) == v:
                routes += 1
                # One captain per route, chosen independently.
                ways = ways * size[v] % MOD
        out.append(f"{routes} {ways}")
    sys.stdout.write("\n".join(out) + "\n")


main()
