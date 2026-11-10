#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from math import gcd
for _ in range(next(it)):
 n=next(it);g=[[] for _ in range(n)]
 for _ in range(n-1):
  u=next(it)-1;v=next(it)-1;g[u].append(v);g[v].append(u)
 a=[next(it) for _ in range(n)];par=[-1]*n;order=[0];par[0]=0
 for u in order:
  for v in g[u]:
   if v!=par[u]:par[v]=u;order.append(v)
 sub=a[:];up=[0]*n
 for u in reversed(order[1:]):sub[par[u]]=gcd(sub[par[u]],sub[u])
 ans=0
 for u in order:
  children=[v for v in g[u] if par[v]==u];ans=max(ans,up[u]+sum(sub[v] for v in children));pref=[gcd(up[u],a[u])]
  for v in children:pref.append(gcd(pref[-1],sub[v]))
  suf=0
  for i in range(len(children)-1,-1,-1):v=children[i];up[v]=gcd(pref[i],suf);suf=gcd(suf,sub[v])
 out.append(str(ans))
print('\n'.join(out))
