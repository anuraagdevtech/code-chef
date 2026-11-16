import sys
from bisect import bisect_left
from math import isqrt


def main() -> None:
    data = list(map(int,sys.stdin.buffer.read().split()))
    maximum = max(data)
    prime = bytearray(b'\x01')*(maximum+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2,isqrt(maximum)+1):
        if prime[p]:
            start = p*p
            prime[start:maximum+1:p] = b'\x00'*((maximum-start)//p+1)
    primes = [i for i in range(2,maximum+1) if prime[i]]
    pos = 1
    out = []
    for _ in range(data[0]):
        n = data[pos]
        pos += 1
        grid = data[pos:pos+n*n]
        pos += n*n
        kinds = bytearray(0 if prime[v] else 1+(v&1) for v in grid)
        seen = bytearray(n*n)
        answer = 0
        for start,p in enumerate(grid):
            if seen[start]:
                continue
            seen[start] = 1
            kind = kinds[start]
            if kind == 0:
                answer += bisect_left(primes,p)
                continue
            answer += p//2 if kind == 1 else p//2+2
            stack = [start]
            while stack:
                u = stack.pop()
                r,c = divmod(u,n)
                for v in (u-n if r else -1,u+n if r+1 < n else -1,
                          u-1 if c else -1,u+1 if c+1 < n else -1):
                    if v >= 0 and not seen[v] and kinds[v] == kind:
                        seen[v] = 1
                        stack.append(v)
        out.append(str(answer))
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
