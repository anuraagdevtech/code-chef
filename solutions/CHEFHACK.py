"""CodeChef CHEFHACK — standalone Python 3 solution."""
import sys
from array import array
from bisect import bisect_left


def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[:2] = b'\x00\x00'
    for p in range(2,int(limit**0.5)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime


prime = sieve(10000000)
primes = array('I',(i for i in range(2,len(prime)) if prime[i]))


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n*n)]
        kind = [2 if prime[x] else x%2 for x in a]
        seen = bytearray(n*n)
        answer = 0
        for start,x in enumerate(a):
            if kind[start] == 2:
                answer += bisect_left(primes,x)
            elif not seen[start]:
                answer += x//2 + (2 if x%2 else 0)
                seen[start] = 1
                stack = [start]
                while stack:
                    v = stack.pop()
                    r,c = divmod(v,n)
                    neighbors = []
                    if r:
                        neighbors.append(v-n)
                    if r+1 < n:
                        neighbors.append(v+n)
                    if c:
                        neighbors.append(v-1)
                    if c+1 < n:
                        neighbors.append(v+1)
                    for u in neighbors:
                        if not seen[u] and kind[u] == kind[start]:
                            seen[u] = 1
                            stack.append(u)
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
