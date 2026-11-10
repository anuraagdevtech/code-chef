"""CodeChef FAMTREE — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    children = [[] for _ in range(n)]
    for i in range(n):
        p = int(next(it))
        if p == -1:
            root = i
        else:
            children[p-1].append(i)
    answer = -10**30
    stack = [(root,a[root],a[root])]
    while stack:
        v, highest, lowest = stack.pop()
        for u in children[v]:
            answer = max(answer, highest-a[u], a[u]-lowest)
            stack.append((u,max(highest,a[u]),min(lowest,a[u])))
    out.append(str(answer if n > 1 else 0))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
