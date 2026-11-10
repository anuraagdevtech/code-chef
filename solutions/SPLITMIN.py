#!/usr/bin/env python3
"""SPLITMIN: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);vals=[];limit=0
 for i in range(n):
  a,b=next(it),next(it);vals.extend(((a,i),(b,i)));limit=max(limit,min(a,b))
 vals.sort();ans=10**30
 for j,(x,i) in enumerate(vals):
  if x<limit:continue
  k=j-1
  while k>=0 and vals[k][1]==i:k-=1
  if k>=0:ans=min(ans,x-vals[k][0])
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
