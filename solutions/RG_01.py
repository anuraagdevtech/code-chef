import sys


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    edges = []
    for _ in range(m):
        u,v,w = next(tokens),next(tokens),next(tokens)
        edges.append((w,u,v))
    edges.sort(reverse=True)
    parent = list(range(n))
    size = [1]*n
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    tree = [[] for _ in range(n)]
    for w,u,v in edges:
        a,b = find(u),find(v)
        if a != b:
            if size[a] < size[b]:
                a,b = b,a
            parent[b] = a
            size[a] += size[b]
            tree[u].append((v,w))
            tree[v].append((u,w))
    for start in range(n):
        answer = [0]*n
        stack = [(start,-1,10**30)]
        while stack:
            u,p,bottleneck = stack.pop()
            for v,w in tree[u]:
                if v != p:
                    answer[v] = min(bottleneck,w)
                    stack.append((v,u,answer[v]))
        print(' '.join(map(str,answer)))

if __name__ == '__main__':
    main()
