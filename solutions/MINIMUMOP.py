#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from math import gcd,isqrt
mx=1000000;spf=list(range(mx+1));primes=[]
for i in range(2,mx+1):
 if spf[i]==i:
  primes.append(i)
  if i<=1000:
   for j in range(i*i,mx+1,i):
    if spf[j]==j:spf[j]=i
for _ in range(next(it)):
 n=next(it);m=next(it);a=[next(it) for _ in range(n)]
 if min(a)==max(a):out.append('0');continue
 g=0
 for x in a:g=gcd(g,x)
 if g>1:out.extend(['1',str(g)]);continue
 bad=set()
 for x in set(a):
  while x>1:
   p=spf[x];bad.add(p)
   while x%p==0:x//=p
 p=next(p for p in primes if p not in bad)
 if p<=m:out.extend(['1',str(p)])
 else:out.extend(['2','2 3'])
print('\n'.join(out))
