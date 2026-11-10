#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from math import gcd
def canonical(n):
 z=n;p=2;f=[];g=0
 while p*p<=z:
  e=0
  while z%p==0:z//=p;e+=1
  if e:f.append((p,e));g=gcd(g,e)
  p=3 if p==2 else p+2
 if z>1:f.append((z,1));g=1
 v=1
 for p,e in f:v*=p**(e//g)
 return v
cache={}
for _ in range(next(it)):
 a=next(it);b=next(it)
 if a not in cache:cache[a]=canonical(a)
 if b not in cache:cache[b]=canonical(b)
 out.append('YES' if cache[a]==cache[b] else 'NO')
print('\n'.join(out))
