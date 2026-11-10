#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
import heapq
for _ in range(next(it)):
 n=next(it);m=next(it);g=[[] for _ in range(n)]
 for _ in range(m):
  u=next(it)-1;v=next(it)-1;g[u].append(v);g[v].append(u)
 # Every purchased edge of length d can be replaced by d unit edges for cost d<=d*d.
 d=[n+1]*n;d[0]=0
 from collections import deque
 q=deque([0])
 while q:
  u=q.popleft()
  for v in g[u]:
   if d[v]>d[u]:d[v]=d[u];q.appendleft(v)
  for v in (u-1,u+1):
   if 0<=v<n and d[v]>d[u]+1:d[v]=d[u]+1;q.append(v)
 out.append(str(d[-1]))
print('\n'.join(out))
