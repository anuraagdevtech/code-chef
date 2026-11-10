"""CodeChef PRIGAME — standalone Python 3 solution."""
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
pi = [0]*1000001
for i in range(1,len(pi)):
    pi[i] = pi[i-1]+prime[i]


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        x,y = int(next(it)),int(next(it))
        out.append('Chef' if pi[x] <= y else 'Divyam')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
