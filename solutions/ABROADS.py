import sys
import heapq


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    n, m, query_count = (int(next(tokens)), int(next(tokens)), int(next(tokens)))
    population = [int(next(tokens)) for _ in range(n)]
    edges = [(int(next(tokens)) - 1, int(next(tokens)) - 1) for _ in range(m)]
    removed = set()
    queries = []
    for _ in range(query_count):
        kind = next(tokens)
        u = int(next(tokens)) - 1
        if kind == b'D':
            removed.add(u)
            queries.append((0, u, 0))
        else:
            x = int(next(tokens))
            queries.append((1, u, population[u]))
            population[u] = x
    parent = list(range(n))
    size = [1] * n
    region = population.copy()
    heap = []

    def root(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def join(u, v):
        u, v = (root(u), root(v))
        if u == v:
            return
        if size[u] < size[v]:
            u, v = (v, u)
        parent[v] = u
        size[u] += size[v]
        region[u] += region[v]
        heapq.heappush(heap, (-region[u], u))
    for i, (u, v) in enumerate(edges):
        if i not in removed:
            join(u, v)
    for i in range(n):
        if parent[i] == i:
            heapq.heappush(heap, (-region[i], i))
    out = []
    for kind, u, old in reversed(queries):
        while parent[heap[0][1]] != heap[0][1] or -heap[0][0] != region[heap[0][1]]:
            heapq.heappop(heap)
        out.append(str(-heap[0][0]))
        if kind:
            r = root(u)
            region[r] += old - population[u]
            population[u] = old
            heapq.heappush(heap, (-region[r], r))
        else:
            join(*edges[u])
    print('\n'.join(reversed(out)))


if __name__ == "__main__":
    main()
