#!/usr/bin/env python3
import sys
from array import array
it=iter(map(int,sys.stdin.buffer.read().split()));cases=[[next(it) for _ in range(next(it))] for _ in range(next(it))];limit=max(map(max,cases),default=1);spf=array('I',[0])*(limit+1)
for p in range(2,int(limit**0.5)+1):
 if not spf[p]:
  for x in range(p*p,limit+1,p):
   if not spf[x]:spf[x]=p
out=[]
for a in cases:
 best={};answer=1
 for x in a:
  factors=[]
  while x>1:
   p=spf[x] or x;factors.append(p)
   while x%p==0:x//=p
  length=1+max((best.get(p,0) for p in factors),default=0)
  for p in factors:best[p]=length
  answer=max(answer,length)
 out.append(str(answer))
print('\n'.join(out))
