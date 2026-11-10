"""CodeChef PETERSEN — standalone Python 3 solution."""
import sys


adj = [[] for _ in range(10)]
for i in range(5):
    for u,v in ((i,(i+1)%5),(i,i+5),(i+5,(i+2)%5+5)):
        adj[u].append(v)
        adj[v].append(u)


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        s = next(it)
        answer = None
        for start in (s[0]-65,s[0]-60):
            path = [start]
            for c in s[1:]:
                candidates = [u for u in adj[path[-1]] if u % 5 == c-65]
                if not candidates:
                    break
                path.append(min(candidates))
            if len(path) == len(s):
                answer = ''.join(map(str,path))
                break
        out.append(answer if answer is not None else '-1')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
