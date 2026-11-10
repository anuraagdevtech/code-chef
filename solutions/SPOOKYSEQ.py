#!/usr/bin/env python3
"""SPOOKYSEQ: standalone Python 3 solution."""
import sys
P=1000000007
fac=[1]*200001
for i in range(1,200001):fac[i]=fac[i-1]*i%P
inv=[1]*200001;inv[-1]=pow(fac[-1],P-2,P)
for i in range(200000,0,-1):inv[i-1]=inv[i]*i%P
from collections import Counter

def solve(it):
 n,m=next(it),next(it);p=list(range(n));sz=[1]*n
 def root(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 for _ in range(m):
  u,v=root(next(it)-1),root(next(it)-1)
  if u!=v:
   if sz[u]<sz[v]:u,v=v,u
   p[v]=u;sz[u]+=sz[v]
 c=Counter((root(i),next(it)) for i in range(n));mod=1000000007;ans=fac[n]
 for i in range(n):
  if p[i]==i:ans=ans*inv[sz[i]]%mod
 for z in c.values():ans=ans*fac[z]%mod
 return str(ans)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
