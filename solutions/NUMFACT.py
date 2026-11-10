"""CodeChef NUMFACT — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        counts = {}
        for _ in range(n):
            x = int(next(it))
            p = 2
            while p*p <= x:
                while x % p == 0:
                    counts[p] = counts.get(p,0)+1
                    x //= p
                p += 1
            if x > 1:
                counts[x] = counts.get(x,0)+1
        answer = 1
        for exponent in counts.values():
            answer *= exponent+1
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
