import sys


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    parent = list(range(n))
    size = [1]*n
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    for _ in range(m):
        u,v = find(next(tokens)-1),find(next(tokens)-1)
        if u != v:
            if size[u] < size[v]:
                u,v = v,u
            parent[v] = u
            size[u] += size[v]
    costs = {}
    for i in range(n):
        cost = next(tokens)
        root = find(i)
        costs.setdefault(root,None)
        if cost >= 0 and (costs[root] is None or cost < costs[root]):
            costs[root] = cost
    if len(costs) == 1:
        print(0)
    elif any(v is None for v in costs.values()):
        print(-1)
    else:
        print(sum(costs.values())+(len(costs)-2)*min(costs.values()))

if __name__ == '__main__':
    main()
