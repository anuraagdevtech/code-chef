#!/usr/bin/env python3
"""SPTREE: standalone Python 3 solution."""
import sys
from collections import deque

def solve(it):
 n,k,a=next(it),next(it),next(it)-1;special=[next(it)-1 for _ in range(k)];g=[[] for _ in range(n)]
 for _ in range(n-1):u,v=next(it)-1,next(it)-1;g[u].append(v);g[v].append(u)
 parent=[-1]*n;d=[0]*n;order=[a];parent[a]=a
 for u in order:
  for v in g[u]:
   if parent[v]<0:parent[v]=u;d[v]=d[u]+1;order.append(v)
 val=[-10**9]*n;who=[-1]*n
 for u in special:val[u]=d[u];who[u]=u
 for u in reversed(order[1:]):
  p=parent[u]
  if val[u]-1>val[p]:val[p]=val[u]-1;who[p]=who[u]
 for u in order[1:]:
  p=parent[u]
  if val[p]-1>val[u]:val[u]=val[p]-1;who[u]=who[p]
 return ' '.join(map(str,val))+'\n'+' '.join(str(x+1) for x in who)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
