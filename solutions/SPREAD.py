"""CodeChef SPREAD — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    n,m,c = int(next(it)),int(next(it)),int(next(it))
    bit = [0]*(n+2)
    for _ in range(m):
        kind = next(it)
        if kind == b'S':
            l,r,k = int(next(it)),int(next(it)),int(next(it))
            for idx,delta in ((l,k),(r+1,-k)):
                while idx <= n:
                    bit[idx] += delta
                    idx += idx & -idx
        else:
            idx = int(next(it))
            answer = c
            while idx:
                answer += bit[idx]
                idx -= idx & -idx
            out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
