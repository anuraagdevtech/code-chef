import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        parent = list(range(n))
        size = [1]*n
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        for _ in range(m):
            u,v = find(int(next(tokens))),find(int(next(tokens)))
            if u != v:
                if size[u] < size[v]:
                    u,v = v,u
                parent[v] = u
                size[u] += size[v]
        for _ in range(int(next(tokens))):
            u,v = find(int(next(tokens))),find(int(next(tokens)))
            out.append('YO' if u == v else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
