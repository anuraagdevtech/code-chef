import sys


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    graph = [[] for _ in range(n)]
    for i in range(m):
        u,v = next(tokens)-1,next(tokens)-1
        graph[u].append((v,i))
        graph[v].append((u,i))
    if any(len(adj)%2 for adj in graph):
        print('NO')
        return
    used = bytearray(m)
    visited = bytearray(n)
    orientation = [None]*m
    stack = [0]
    visited[0] = 1
    while stack:
        u = stack[-1]
        while graph[u] and used[graph[u][-1][1]]:
            graph[u].pop()
        if not graph[u]:
            stack.pop()
            continue
        v,e = graph[u].pop()
        used[e] = 1
        orientation[e] = (u+1,v+1)
        visited[v] = 1
        stack.append(v)
    if not all(visited) or not all(used):
        print('NO')
        return
    print('YES')
    sys.stdout.write('\n'.join(f'{u} {v}' for u,v in orientation)+'\n')

if __name__ == '__main__':
    main()
