#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[];p=1000000007
# Before its final character, a valid string consists of blocks 1 or 221.
transition=({49:0,50:1},{50:2},{49:0})
for _ in range(int(next(it))):
 a,b=next(it),next(it);dp={(0,0):1}
 for x,y in zip(a[:-1],b[:-1]):
  nd={}
  for (u,v),count in dp.items():
   for c,d in ((x,y),(y,x)):
    if c in transition[u] and d in transition[v]:
     state=(transition[u][c],transition[v][d]);nd[state]=(nd.get(state,0)+count)%p
  dp=nd
 out.append(str(dp.get((0,0),0)*2%p))
print('\n'.join(out))
