"""CodeChef TAAPLUSB — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        answer = n/2 - (1-10.0**(-min(n,20)))/18
        out.append(f'{answer:.10f}')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
