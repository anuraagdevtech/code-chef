import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        answer = [0]*n
        answer[0] = 1
        stack = [0]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if answer[v] == 0:
                    answer[v] = 3-answer[u]
                    stack.append(v)
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
