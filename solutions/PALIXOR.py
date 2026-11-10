#!/usr/bin/env python3
import sys
from collections import Counter
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
pal=[x for x in range(32768) if str(x)==str(x)[::-1]]
def transform(a):
 h=1;n=len(a)
 while h<n:
  for j in range(0,n,2*h):
   for i in range(j,j+h):x=a[i];y=a[i+h];a[i]=x+y;a[i+h]=x-y
  h*=2
for _ in range(next(it)):
 n=next(it);f=Counter(next(it) for _ in range(n))
 if len(f)*len(pal)<1500000:
  total=sum(v*f.get(x^p,0) for x,v in f.items() for p in pal)
 else:
  a=[0]*32768
  for x,v in f.items():a[x]=v
  transform(a);a=[x*x for x in a];transform(a)
  total=sum(a[p] for p in pal)//32768
 out.append(str((total+n)//2))
print('\n'.join(out))
