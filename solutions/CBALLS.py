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
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        limit = max(a)
        frequency = [0]*(limit+1)
        running = 0
        for value in a:
            running = max(running,value)
            frequency[running] += 1
        for value in range(1,limit+1):
            frequency[value] += frequency[value-1]
        original_sum = sum(a)
        answer = 10**30
        prime = sieve(limit+1)
        for p in range(2,limit+2):
            if not prime[p]:
                continue
            rounded_sum = 0
            for upper in range(p,limit+p,p):
                count = frequency[min(upper,limit)]-frequency[upper-p]
                rounded_sum += upper*count
            answer = min(answer,rounded_sum-original_sum)
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
