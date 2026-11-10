"""CodeChef SVRT — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, k = int(next(it)), int(next(it))
        d = (n+k-1)//k
        out.append(f'{d} {n-k*(d-1)}')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
