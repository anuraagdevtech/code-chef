#!/usr/bin/env python3
"""ANUMLA: standalone Python 3 solution."""
import sys
from collections import Counter

def solve(it):
 n=next(it); a=sorted(next(it) for _ in range(1<<n)); c=Counter(a); c[0]-=1
 sums=[0]; ans=[]
 for x in a:
  if c[x]:
   ans.append(x); new=[v+x for v in sums]
   for v in new:c[v]-=1
   sums+=new
 return ' '.join(map(str,ans))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
