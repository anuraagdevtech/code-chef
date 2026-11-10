"""CodeChef CHEFELEC — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        s = next(it)
        x = [int(next(it)) for _ in range(n)]
        answer = x[-1] - x[0]
        last = s.index(49)
        gap = 0
        for i in range(last+1, n):
            gap = max(gap, x[i]-x[i-1])
            if s[i] == 49:
                answer -= gap
                gap = 0
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
