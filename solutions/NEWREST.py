#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));cases=[(next(it),next(it),next(it)) for _ in range(next(it))];p=1000000007;mx=max((n for n,m,k in cases),default=0);by={}
for i,c in enumerate(cases):by.setdefault(c[0],[]).append((i,c[1],c[2]))
s=[1]+[0]*mx;ans=[0]*len(cases)
for n in range(1,mx+1):
 for j in range(n,0,-1):s[j]=(s[j]*j+s[j-1])%p
 s[0]=0
 for i,m,k in by.get(n,[]):
  fall=1;v=0
  for j in range(1,min(n,m,k)+1):fall=fall*(m-j+1)%p;v=(v+fall*s[j])%p
  ans[i]=v
print('\n'.join(map(str,ans)))
