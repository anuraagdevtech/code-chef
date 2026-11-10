"""CodeChef ABX01 — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        a, n = int(next(it)), int(next(it))
        out.append(str(pow(a,n,9) or 9))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
