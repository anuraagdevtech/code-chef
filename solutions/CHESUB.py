#!/usr/bin/env python3
"""CHESUB: standalone Python 3 solution."""
import sys
def solve(it):
 n,k=next(it),next(it);a=[next(it) for _ in range(n)];neg=-10**30;best=[neg]*(k+1);end=best.copy();best[0]=0
 for x in a:
  for j in range(k,0,-1):
   end[j]=max(end[j],best[j-1])+j*x;best[j]=max(best[j],end[j])
 return str(best[k])

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
