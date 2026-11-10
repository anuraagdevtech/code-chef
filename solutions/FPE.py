#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from math import gcd
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];g=[[] for _ in range(n)]
 for i in range(n-1):
  u=next(it)-1;v=next(it)-1;g[u].append(v);g[v].append(u)
 par=[-1]*n;order=[0];par[0]=0
 for u in order:
  for v in g[u]:
   if v!=par[u]:par[v]=u;order.append(v)
 sub=a[:];sums=[0]*n
 for u in reversed(order[1:]):p=par[u];sub[p]=gcd(sub[p],sub[u]);sums[p]+=sub[u]
 best=[0]*n
 for u in reversed(order):
  best[u]=sums[u]+max([0]+[best[v]-sub[v] for v in g[u] if par[v]==u])
 out.append(str(best[0]))
print('\n'.join(out))
