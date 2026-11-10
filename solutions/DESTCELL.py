"""CodeChef DESTCELL — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,m = int(next(it)),int(next(it))
        cells = n*m
        answer = []
        for step in range(1,cells+1):
            count = (cells-1)//step+1
            shared = 0
            for idx in range(0,cells,step):
                r,c = divmod(idx,m)
                shared += (c*n+r)%step == 0
            answer.append(2*count-shared)
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
