"""CodeChef KCON — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, k = int(next(it)), int(next(it))
        a = [int(next(it)) for _ in range(n)]
        current = answer = a[0]
        for i in range(1, n*min(k,2)):
            x = a[i % n]
            current = max(x, current+x)
            answer = max(answer, current)
        if k > 2:
            answer += max(0, sum(a))*(k-2)
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
