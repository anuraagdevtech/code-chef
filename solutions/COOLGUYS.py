"""CodeChef COOLGUYS — standalone Python 3 solution."""
import sys
from math import gcd,isqrt



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        root = isqrt(n)
        numerator = 2*sum(n//i for i in range(1,root+1))-root*root
        denominator = n*n
        common = gcd(numerator,denominator)
        out.append(f'{numerator//common}/{denominator//common}')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
