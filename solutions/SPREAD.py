import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n,m,initial = (int(next(tokens)) for _ in range(3))
    tree = [0]*(n+1)
    def add(index,value):
        while index <= n:
            tree[index] += value
            index += index&-index
    out = []
    for _ in range(m):
        kind = next(tokens)
        if kind == b'S':
            u,v,k = (int(next(tokens)) for _ in range(3))
            add(u,k)
            add(v+1,-k)
        else:
            index = int(next(tokens))
            total = initial
            while index:
                total += tree[index]
                index -= index&-index
            out.append(str(total))
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
