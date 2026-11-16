import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,root,t = (int(next(tokens)) for _ in range(3))
        root -= 1
        graph = []
        for _ in range(n):
            degree = int(next(tokens))
            graph.append([int(next(tokens))-1 for _ in range(degree)])
        marked = {int(next(tokens))-1 for _ in range(t)}
        parent = [-2]*n
        parent[root] = -1
        order = [root]
        for u in order:
            for v in graph[u]:
                if parent[v] == -2:
                    parent[v] = u
                    order.append(v)
        safe = [False]*n
        for u in reversed(order):
            children = [v for v in graph[u] if parent[v] == u]
            safe[u] = u not in marked and (len(children) < 2 or any(safe[v] for v in children))
        out.append('yes' if safe[root] else 'no')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
