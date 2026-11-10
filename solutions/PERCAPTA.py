"""CodeChef PERCAPTA — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,m = int(next(it)),int(next(it))
        a = [int(next(it)) for _ in range(n)]
        b = [int(next(it)) for _ in range(n)]
        best = 0
        for v in range(1,n):
            if a[v]*b[best] > a[best]*b[v]:
                best = v
        allowed = [a[v]*b[best] == a[best]*b[v] for v in range(n)]
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u,v = int(next(it))-1,int(next(it))-1
            if allowed[u] and allowed[v]:
                adj[u].append(v)
                adj[v].append(u)
        answer = []
        for start in range(n):
            if not allowed[start]:
                continue
            allowed[start] = False
            component = [start]
            for v in component:
                for u in adj[v]:
                    if allowed[u]:
                        allowed[u] = False
                        component.append(u)
            if len(component) > len(answer):
                answer = component
        out.append(str(len(answer)))
        out.append(' '.join(str(v+1) for v in answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
