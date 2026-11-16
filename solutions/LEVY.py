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
    primes = [i for i,v in enumerate(sieve(limit)) if v]
    answers = [0]*(limit+1)
    for q in primes:
        if 2*q+2 > limit:
            break
        for p in primes:
            total = p+2*q
            if total > limit:
                break
            answers[total] += 1
    sys.stdout.write('\n'.join(str(answers[n]) for n in values[1:])+'\n')

if __name__ == '__main__':
    main()
