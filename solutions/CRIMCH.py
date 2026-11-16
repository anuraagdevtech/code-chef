import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        colour = [-1]*n
        possible = True
        for start in range(n):
            if colour[start] != -1:
                continue
            colour[start] = 0
            stack = [start]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if colour[v] == -1:
                        colour[v] = colour[u]^1
                        stack.append(v)
                    elif colour[v] == colour[u]:
                        possible = False
        out.append('YES' if possible else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
