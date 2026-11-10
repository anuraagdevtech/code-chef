"""CodeChef OMWG — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n,m = int(next(it)),int(next(it))
        out.append(str(n*(m-1)+m*(n-1)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
