#!/usr/bin/env python3
"""ABROADS: standalone Python 3 solution."""
import sys
import heapq

def main():
 it=iter(sys.stdin.buffer.read().split());n,m,q=int(next(it)),int(next(it)),int(next(it));a=[int(next(it)) for _ in range(n)];edges=[(int(next(it))-1,int(next(it))-1) for _ in range(m)];removed=set();queries=[]
 for _ in range(q):
  kind=next(it);u=int(next(it))-1
  if kind==b'D':removed.add(u);queries.append((0,u,0))
  else:x=int(next(it));queries.append((1,u,a[u]));a[u]=x
 p=list(range(n));sz=[1]*n;val=a.copy();h=[]
 def root(x):
  while x!=p[x]:p[x]=p[p[x]];x=p[x]
  return x
 def join(u,v):
  u,v=root(u),root(v)
  if u==v:return
  if sz[u]<sz[v]:u,v=v,u
  p[v]=u;sz[u]+=sz[v];val[u]+=val[v];heapq.heappush(h,(-val[u],u))
 for i,(u,v) in enumerate(edges):
  if i not in removed:join(u,v)
 for i in range(n):
  if p[i]==i:heapq.heappush(h,(-val[i],i))
 out=[]
 for kind,u,old in reversed(queries):
  while p[h[0][1]]!=h[0][1] or -h[0][0]!=val[h[0][1]]:heapq.heappop(h)
  out.append(str(-h[0][0]))
  if kind:r=root(u);val[r]+=old-a[u];a[u]=old;heapq.heappush(h,(-val[r],r))
  else:join(*edges[u])
 print('\n'.join(reversed(out)))

if __name__ == '__main__':
 main()
