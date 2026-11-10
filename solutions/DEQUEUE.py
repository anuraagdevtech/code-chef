#!/usr/bin/env python3
"""DEQUEUE: standalone Python 3 solution."""
import sys
def solve(it):
 n,m=next(it),next(it);a=[next(it)-1 for _ in range(m)];total=[0]*n
 for x in a:total[x]+=1
 c=[0]*n;l=best=0
 for r,x in enumerate(a):
  c[x]+=1
  while c[x]==total[x]:c[a[l]]-=1;l+=1
  best=max(best,r-l+1)
 return str(m-best)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
