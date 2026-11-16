import sys
from math import isqrt

def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime


def main() -> None:
    values = list(map(int,sys.stdin.buffer.read().split()))
    limit = max(values[1:])
    prime = sieve(limit)
    prefix = [0]*(limit+1)
    for c in range(1,limit+1):
        prefix[c] = prefix[c-1]+int(c >= 5 and prime[c] and prime[c-2])
    sys.stdout.write('\n'.join(str(prefix[n]) for n in values[1:])+'\n')

if __name__ == '__main__':
    main()
