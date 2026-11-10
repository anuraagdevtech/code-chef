"""CodeChef PCJ18C — standalone Python 3 solution."""
import sys
from math import gcd



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, a, k = int(next(it)), int(next(it)), int(next(it))
        den = n*(n-1)
        num = a*den + (k-1)*(360*(n-2)-2*n*a)
        g = gcd(num, den)
        out.append(f'{num//g} {den//g}')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
