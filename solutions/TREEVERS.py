import sys
from functools import cmp_to_key


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        w = [int(next(tokens)) for _ in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1]*n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        ones = w[:]
        zeros = [1-x for x in w]
        inversions = [0]*n
        def compare(a,b):
            left,right = ones[a]*zeros[b],ones[b]*zeros[a]
            return (left > right)-(left < right)
        for u in reversed(order):
            children = sorted((v for v in graph[u] if v != parent[u]),key=cmp_to_key(compare))
            for v in children:
                inversions[u] += inversions[v]+ones[u]*zeros[v]
                ones[u] += ones[v]
                zeros[u] += zeros[v]
        out.append(str(inversions[0]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
