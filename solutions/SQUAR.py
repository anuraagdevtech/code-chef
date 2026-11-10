#!/usr/bin/env python3
"""SQUAR: standalone Python 3 solution."""
import sys
from array import array
raw=list(map(int,sys.stdin.buffer.read().split()));V=max(raw);spf=array('I',[0])*(V+1)
for i in range(2,int(V**0.5)+1):
 if not spf[i]:
  for j in range(i*i,V+1,i):
   if not spf[j]:spf[j]=i
from collections import Counter

def solve(it):
 n=next(it);c=Counter()
 for _ in range(n):
  x=next(it);kernel=1
  while x>1:
   p=spf[x] or x;odd=0
   while x%p==0:x//=p;odd^=1
   if odd:kernel*=p
  if kernel!=1:c[kernel]+=1
 return str(max(c.values(),default=0))

if __name__ == '__main__':
 it=iter(raw)
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
