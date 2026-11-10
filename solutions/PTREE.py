#!/usr/bin/env python3
import sys
from bisect import bisect_left
from collections import defaultdict
from math import isqrt
it=iter(map(int,sys.stdin.buffer.read().split()));out=[];p=1000000007
for _ in range(next(it)):
 n,q=next(it),next(it);g=[[] for _ in range(n)]
 for _ in range(n-1):u,v=next(it)-1,next(it)-1;g[u].append(v);g[v].append(u)
 parent=[-1]*n;depth=[0]*n;order=[0]
 for v in order:
  for u in g[v]:
   if u!=parent[v]:parent[u]=v;depth[u]=depth[v]+1;order.append(u)
 children=[[] for _ in range(n)]
 for v in order[1:]:children[parent[v]].append(v)
 tin=[0]*n;tout=[0]*n;timer=0;stack=[(0,0)];special=defaultdict(list);height=max(depth)
 while stack:
  v,exit=stack.pop()
  if exit:tout[v]=timer;continue
  tin[v]=timer;timer+=1;stack.append((v,1))
  if len(children[v])>1:special[depth[v]+1].append((tin[v],len(children[v])-1))
  for u in reversed(children[v]):stack.append((u,0))
 levels=sorted(special);rows={}
 for d,items in special.items():
  items.sort();positions=[];pref=[0]
  for pos,w in items:positions.append(pos);pref.append(pref[-1]+w)
  rows[d]=(positions,pref)
 anchor=list(range(n))
 for v in reversed(order):
  if len(children[v])==1:anchor[v]=anchor[children[v][0]]
 del g,parent,children,order,special
 cache={};answer=0
 def geom(r,count):
  result=0;power=1;block=1
  while count:
   if count&1:result=(result+power*block)%p;power=power*r%p
   block=block*(1+r)%p;r=r*r%p;count//=2
  return result
 for _ in range(q):
  a,b=next(it),next(it);v=(a^answer)-1;y=b^answer
  root=anchor[v];delta=depth[root]-depth[v]
  if root not in cache:
   segments=[];last=depth[root];width=1
   for d in levels[bisect_left(levels,depth[root]+1):]:
    positions,pref=rows[d];gain=pref[bisect_left(positions,tout[root])]-pref[bisect_left(positions,tin[root])]
    if gain:segments.append((last-depth[root],d-last,width));last=d;width+=gain
   segments.append((last-depth[root],height-last+1,width));cache[root]=segments
  segments=cache[root];answer=0
  if delta:segments=[(0,segments[0][1]+delta,1)]+[(start+delta,length,width) for start,length,width in segments[1:]]
  if y==1:
   answer=sum(width*length*(2*start+length-1)//2 for start,length,width in segments)%p
  else:
   inv=pow(y-1,p-2,p);power=1
   if len(segments)>16:
    limit=isqrt(tout[v]-tin[v])+1;small=[1]*limit
    for i in range(1,limit):small[i]=small[i-1]*y%p
    step=small[-1]*y%p;large=[1]*(limit+1)
    for i in range(1,limit+1):large[i]=large[i-1]*step%p
    def powerof(exponent):return large[exponent//limit]*small[exponent%limit]%p
   else:
    def powerof(exponent):return pow(y,exponent,p)
   for start,length,width in segments:
    r=powerof(width)
    if length==1:endpower=r;s=1
    else:endpower=powerof(width*length);s=geom(r,length)
    answer=(answer+power*((start+length-1)*endpower-(start-1)-s))%p;power=power*endpower%p
   answer=answer*inv%p
  out.append(str(answer))
print('\n'.join(out))
