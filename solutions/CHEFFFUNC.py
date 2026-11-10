#!/usr/bin/env python3
"""CHEFFFUNC: standalone Python 3 solution."""
import sys
def solve(it):
 l,r=next(it),next(it);ans=0
 for j in range(r.bit_length()+1):
  x=((l+(1<<j)-1)>>j)<<j
  if x<=r:
   k=x.bit_length();ans=max(ans,3*(1<<(k-1))-1-x+k-x.bit_count())
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
