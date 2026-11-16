import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        indegree = [0]*n
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            indegree[v] += 1
        out.append(str(sum(d == 0 for d in indegree)-1))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
