#!/usr/bin/env python3
"""EXISTENCEOFX: standalone Python 3 solution."""
import sys
def solve(it):
 a,b,c=next(it),next(it),next(it); carry=0
 for k in range(29):
  av=(a>>k)&1; bv=(b>>k)&1; cv=(c>>k)&1
  x=av^bv^cv^carry
  carry=((av^x)+(bv^x)+carry)>>1
 return 'YES' if carry==0 else 'NO'

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
