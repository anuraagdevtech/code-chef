"""CodeChef SUMQ — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        p, q, r = int(next(it)), int(next(it)), int(next(it))
        a = sorted(int(next(it)) for _ in range(p))
        b = sorted(int(next(it)) for _ in range(q))
        c = sorted(int(next(it)) for _ in range(r))
        i = j = sa = sc = answer = 0
        mod = 1000000007
        for y in b:
            while i < p and a[i] <= y:
                sa += a[i]
                i += 1
            while j < r and c[j] <= y:
                sc += c[j]
                j += 1
            answer = (answer + (sa+i*y)*(sc+j*y)) % mod
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
