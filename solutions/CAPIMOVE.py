import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        population = [int(next(tokens)) for _ in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u, v = int(next(tokens))-1, int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        order = sorted(range(n), key=population.__getitem__, reverse=True)
        marks = [-1]*n
        answer = []
        for u in range(n):
            marks[u] = u
            for v in graph[u]:
                marks[v] = u
            capital = next((v+1 for v in order if marks[v] != u), 0)
            answer.append(capital)
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
