#!/usr/bin/env python3
"""CLASSES: standalone Python 3 solution."""
import sys
from collections import deque

def solve(it):
 n,m,s,k=next(it),next(it),next(it),next(it);g=[[] for _ in range(n+1)]
 for _ in range(m):u,v=next(it),next(it);g[u].append(v);g[v].append(u)
 d=[-1]*(n+1);d[0]=0;q=deque([0])
 while q:
  u=q.popleft()
  for v in g[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 a=sorted(d[next(it)] for _ in range(s))
 return str(2*sum(a[:k]))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
