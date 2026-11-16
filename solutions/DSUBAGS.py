import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n,q = int(next(tokens)),int(next(tokens))
    parent = list(range(n))
    size = [1]*n
    components = n
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    out = []
    for _ in range(q):
        kind = int(next(tokens))
        if kind == 3:
            out.append(str(components))
            continue
        u,v = find(int(next(tokens))-1),find(int(next(tokens))-1)
        if kind == 2:
            out.append('YES' if u == v else 'NO')
        elif u != v:
            if size[u] < size[v]:
                u,v = v,u
            parent[v] = u
            size[u] += size[v]
            components -= 1
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
