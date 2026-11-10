"""CodeChef EARTSEQ — standalone Python 3 solution."""
import sys


def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[:2] = b'\x00\x00'
    for p in range(2,int(limit**0.5)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime


prime = sieve(1000000)
primes = [i for i in range(13,len(prime)) if prime[i]]


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        edges = []
        palette = [2,3,5,7,11]
        for i in range(n):
            banned = set(edges[-2:])
            if i >= n-2:
                banned.update(edges[:i-(n-2)+1])
            edges.append(next(p for p in palette if p not in banned))
        answer = [edges[i]*edges[(i+1)%n]*primes[i] for i in range(n)]
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
