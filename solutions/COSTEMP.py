import sys
from array import array


def main() -> None:
    values = map(int,sys.stdin.buffer.read().split())
    n = next(values)
    head = array('i',[-1])*n
    to = array('i')
    link = array('i')
    def edge(u,v):
        to.append(v)
        link.append(head[u])
        head[u] = len(to)-1
    for _ in range(n-1):
        u,v = next(values),next(values)
        edge(u,v)
        edge(v,u)
    del values
    parent = array('i',[-1])*n
    depth = array('i',[0])*n
    order = array('i',[0])
    for u in order:
        e = head[u]
        while e != -1:
            v = to[e]
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u]+1
                order.append(v)
            e = link[e]
    size = array('i',[1])*n
    for u in reversed(order[1:]):
        size[parent[u]] += size[u]
    answer = [0]*n
    answer[0] = sum(depth)
    for u in order[1:]:
        answer[u] = answer[parent[u]]+n-2*size[u]
    print(' '.join(map(str,answer)))

if __name__ == '__main__':
    main()
