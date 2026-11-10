"""CodeChef CBALLS — standalone Python 3 solution."""
import sys


def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[:2] = b'\x00\x00'
    for p in range(2,int(limit**0.5)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime


prime = sieve(10010)
primes = [i for i in range(2,len(prime)) if prime[i]]


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        maximum = 0
        base = 0
        counts = {}
        for x in a:
            maximum = max(maximum,x)
            base += maximum-x
            counts[maximum] = counts.get(maximum,0)+1
        extra = 10**30
        for p in primes:
            value = sum(((-x)%p)*count for x,count in counts.items())
            extra = min(extra,value)
            if p >= maximum:
                break
        out.append(str(base+extra))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
