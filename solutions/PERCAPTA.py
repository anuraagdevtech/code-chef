import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        b = [int(next(tokens)) for _ in range(n)]
        best = 0
        for i in range(1,n):
            if a[i]*b[best] > a[best]*b[i]:
                best = i
        eligible = [a[i]*b[best] == a[best]*b[i] for i in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            if eligible[u] and eligible[v]:
                graph[u].append(v)
                graph[v].append(u)
        seen = [False]*n
        answer = []
        for start in range(n):
            if not eligible[start] or seen[start]:
                continue
            component = [start]
            seen[start] = True
            for u in component:
                for v in graph[u]:
                    if not seen[v]:
                        seen[v] = True
                        component.append(v)
            if len(component) > len(answer):
                answer = component
        out.append(str(len(answer)))
        out.append(' '.join(str(i+1) for i in answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
