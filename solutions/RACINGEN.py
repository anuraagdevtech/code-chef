"""CodeChef RACINGEN — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        x, r, m = int(next(it)), int(next(it)), int(next(it))
        run = 60 * r
        out.append('YES' if run + max(0, run-x) <= 60*m else 'NO')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
