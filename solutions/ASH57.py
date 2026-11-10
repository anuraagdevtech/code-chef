#!/usr/bin/env python3
"""ASH57: standalone Python 3 solution."""
import sys
from bisect import bisect_left

def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];ca=[next(it) for _ in range(n)];b=[next(it) for _ in range(n)];cb=[next(it) for _ in range(n)];active=set(cb);groups={}
 for x,c in zip(a,ca):
  if c in active:groups.setdefault(c,[]).append(x)
 for x,c in zip(b,cb):groups.setdefault(c,[]).append(x)
 for v in groups.values():v.sort()
 pos={};prev=-1;ok=True
 for x,c in zip(a,ca):
  if c in active:
   v=groups[c];j=bisect_left(v,prev,pos.get(c,0))
   if j==len(v):ok=False;break
   x=v[j];pos[c]=j+1
  if x<prev:ok=False;break
  prev=x
 return 'Yes' if ok else 'No'

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
