#!/usr/bin/env python3
"""CNCTCT: standalone Python 3 solution."""
import sys
def solve(it):
 n=next(it);a=[next(it) for _ in range(n)];p=list(range(n));sz=[1]*n;components=n;ans=0
 def root(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 for b in range(30):
  first=-1
  for i,x in enumerate(a):
   if x>>b&1:
    if first<0:first=i;continue
    u,v=root(first),root(i)
    if u!=v:
     if sz[u]<sz[v]:u,v=v,u
     p[v]=u;sz[u]+=sz[v];components-=1;ans+=1<<b
 return str(ans if components==1 else -1)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
