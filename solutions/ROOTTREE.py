"""CodeChef ROOTTREE — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        indegree = [0]*n
        for _ in range(n-1):
            u, v = int(next(it))-1, int(next(it))-1
            indegree[v] += 1
        out.append(str(indegree.count(0)-1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
