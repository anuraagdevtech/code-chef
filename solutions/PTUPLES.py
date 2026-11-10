"""CodeChef PTUPLES — standalone Python 3 solution."""
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
twins = [0]*1000001
for i in range(1,1000001):
    twins[i] = twins[i-1]+int(i >= 5 and prime[i] and prime[i-2])


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        out.append(str(twins[n]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
