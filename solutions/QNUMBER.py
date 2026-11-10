#!/usr/bin/env python3
import sys
from math import gcd
it=iter(map(int,sys.stdin.buffer.read().split()));n=next(it);q=next(it);z=n;fac=[];p=2
while p*p<=z:
 e=0
 while z%p==0:z//=p;e+=1
 if e:fac.append((p,e))
 p=3 if p==2 else p+2
if z>1:fac.append((z,1))
total=1
for p,e in fac:total*=e+1
out=[]
for _ in range(q):
 t=next(it);k=next(it)
 if t==1:
  k=gcd(n,k);ans=1
  for p,e in fac:
   v=0
   while k%p==0:k//=p;v+=1
   ans*=v+1
 else:
  ans=0
  if n%k==0:
   ans=1
   for p,e in fac:
    v=0
    while k%p==0:k//=p;v+=1
    ans*=e-v+1
  if t==3:ans=total-ans
 out.append(str(ans))
print('\n'.join(out))
