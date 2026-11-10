#!/usr/bin/env python3
"""EXPECTEDSUM: standalone Python 3 solution."""
import sys
def solve(it):
 a,b=next(it),next(it);n=a+b;p=998244353
 return str(a*((n+1)//2)*pow(n,p-2,p)%p)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
