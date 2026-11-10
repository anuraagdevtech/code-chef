"""CodeChef LEVY — standalone Python 3 solution."""
import sys


def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[:2] = b'\x00\x00'
    for p in range(2,int(limit**0.5)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime


prime = sieve(10000)
primes = [p for p in range(2,10001) if prime[p]]
ways = [0]*10001
for q in primes:
    for p in primes:
        value = p+2*q
        if value > 10000:
            break
        ways[value] += 1


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        out.append(str(ways[n]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
