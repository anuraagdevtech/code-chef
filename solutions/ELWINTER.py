#!/usr/bin/env python3
import sys,heapq
it=iter(map(int,sys.stdin.buffer.read().split()));n=next(it);m=next(it);q=next(it)
g=[[] for _ in range(n)]
for _ in range(m):
 u=next(it)-1;v=next(it)-1;g[u].append(v);g[v].append(u)
f=[False]*n;h=[];now=0;out=[]
for _ in range(q):
 typ=next(it);x=next(it)
 if typ==1:
  if not f[x-1]: f[x-1]=True;heapq.heappush(h,(now,x-1))
 elif typ==2:
  now+=x
  while h and h[0][0]<now:
   t,u=heapq.heappop(h)
   for v in g[u]:
    if not f[v]: f[v]=True;heapq.heappush(h,(t+1,v))
 else: out.append('YES' if f[x-1] else 'NO')
print('\n'.join(out))
