#!/usr/bin/env python3
"""ANTSCHEF: standalone Python 3 solution."""
import sys
from collections import Counter

def solve(it):
 n=next(it);lines=[];freq=Counter()
 for _ in range(n):
  k=next(it);a=[next(it) for _ in range(k)];lines.append(a);freq.update(abs(x) for x in a)
 ans=sum(v>1 for v in freq.values())
 for a in lines:
  neg=sum(x<0 for x in a);pos=len(a)-neg
  for x in sorted(a,key=abs):
   if x<0:neg-=1
   else:pos-=1
   if freq[abs(x)]>1:ans+=neg if x<0 else pos
   else:ans+=pos if x<0 else neg
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
