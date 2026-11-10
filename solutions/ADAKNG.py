"""CodeChef ADAKNG — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        r, c, k = int(next(it)), int(next(it)), int(next(it))
        rows = min(8,r+k)-max(1,r-k)+1
        cols = min(8,c+k)-max(1,c-k)+1
        out.append(str(rows*cols))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
