import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        maps = int(next(tokens))
        left = [-1]
        right = [-1]
        count = [0]
        depth = [0]
        for _ in range(maps):
            n = int(next(tokens))
            children = [[] for _ in range(n)]
            for _ in range(n-1):
                u,side,v = int(next(tokens))-1,next(tokens),int(next(tokens))-1
                children[u].append((side,v))
            count[0] += 1
            stack = [(0,0)]
            while stack:
                u,node = stack.pop()
                for side,v in children[u]:
                    branch = left if side == b'L' else right
                    if branch[node] == -1:
                        branch[node] = len(count)
                        left.append(-1)
                        right.append(-1)
                        count.append(0)
                        depth.append(depth[node]+1)
                    target = branch[node]
                    count[target] += 1
                    stack.append((v,target))
        answer = [0]*(maps+1)
        for c,d in zip(count,depth):
            answer[c] = max(answer[c],d)
        for k in range(maps-1,0,-1):
            answer[k] = max(answer[k],answer[k+1])
        out.append(' '.join(map(str,answer[1:])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
