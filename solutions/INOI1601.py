import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n = int(next(tokens))
    wealth = [int(next(tokens)) for _ in range(n)]
    children = [[] for _ in range(n)]
    root = 0
    for i in range(n):
        p = int(next(tokens))
        if p == -1:
            root = i
        else:
            children[p-1].append(i)
    answer = -10**30
    stack = [(root, wealth[root])]
    while stack:
        u, highest = stack.pop()
        for v in children[u]:
            answer = max(answer, highest-wealth[v])
            stack.append((v,max(highest,wealth[v])))
    print(answer if n > 1 else 0)

if __name__ == '__main__':
    main()
