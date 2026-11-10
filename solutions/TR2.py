"""CodeChef TR2 — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        maps = int(next(it))
        trie = [[-1,-1]]
        count = [0]
        depth = [0]
        for _ in range(maps):
            n = int(next(it))
            children = [[] for _ in range(n)]
            indegree = [0]*n
            for _ in range(n-1):
                u,c,v = int(next(it))-1,next(it),int(next(it))-1
                children[u].append((v,0 if c == b'L' else 1))
                indegree[v] += 1
            root = indegree.index(0)
            stack = [(root,0)]
            while stack:
                v,p = stack.pop()
                count[p] += 1
                for u,c in children[v]:
                    if trie[p][c] < 0:
                        trie[p][c] = len(trie)
                        trie.append([-1,-1])
                        count.append(0)
                        depth.append(depth[p]+1)
                    stack.append((u,trie[p][c]))
        answer = [0]*(maps+1)
        for c,d in zip(count,depth):
            answer[c] = max(answer[c],d)
        for k in range(maps-1,0,-1):
            answer[k] = max(answer[k],answer[k+1])
        out.append(' '.join(map(str,answer[1:])))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
