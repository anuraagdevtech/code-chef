"""CodeChef SPCTRIPS — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        answer = 0
        for c in range(1,n//2+1):
            for b in range(2*c,n+1,c):
                answer += (n-c)//b+1
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
