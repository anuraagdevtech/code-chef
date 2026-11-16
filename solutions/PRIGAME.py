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
    queries = list(zip(values[1::2],values[2::2]))
    limit = max(x for x,_ in queries)
    prime = sieve(limit)
    prefix = [0]*(limit+1)
    for x in range(1,limit+1):
        prefix[x] = prefix[x-1]+prime[x]
    sys.stdout.write('\n'.join('Chef' if prefix[x] <= y else 'Divyam' for x,y in queries)+'\n')

if __name__ == '__main__':
    main()
