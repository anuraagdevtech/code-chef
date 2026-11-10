#!/usr/bin/env python3
"""BALSUFF: standalone Python 3 solution."""
import sys
from collections import Counter

def solve(it):
 n,k=int(next(it)),int(next(it));c=Counter(next(it).decode());chars=sorted(c);out=[]
 if max(c.values())-min(c.values())>k:return '-1'
 for _ in range(n):
  mx=max(c.values())
  for x in chars:
   if c[x] and mx-(c[x]-1)<=k:c[x]-=1;out.append(x);break
 return ''.join(out)

if __name__ == '__main__':
 it=iter(sys.stdin.buffer.read().split())
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
