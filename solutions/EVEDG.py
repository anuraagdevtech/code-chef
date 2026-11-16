import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        degree = [0]*n
        first = None
        for _ in range(m):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            degree[u] += 1
            degree[v] += 1
            if first is None:
                first = (u,v)
        labels = [1]*n
        if m%2 == 0:
            k = 1
        else:
            odd = next((u for u in range(n) if degree[u]%2),None)
            if odd is not None:
                k = 2
                labels[odd] = 2
            else:
                k = 3
                u,v = first
                labels[u],labels[v] = 2,3
        out.append(str(k))
        out.append(' '.join(map(str,labels)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
