"""CodeChef MONKS — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        a = sorted(int(next(it)) for _ in range(n))
        total = sum(a)
        keep = max(i for i,x in enumerate(a, 1) if i*x <= total)
        out.append(str(n-keep))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
