#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
import heapq
for _ in range(next(it)):
 n=next(it);b=[next(it) for _ in range(n)];last={v:i for i,v in enumerate(b) if v>=0}
 h=[v for v in range(n+1) if v not in last];heapq.heapify(h);seen=bytearray(n+2);mex=0;a=[];ok=True
 for i,v in enumerate(b):
  x=heapq.heappop(h);a.append(x);seen[x]=1
  while seen[mex]:mex+=1
  if v>=0 and v!=mex:ok=False
  if v>=0 and last[v]==i:heapq.heappush(h,v)
 out.append(' '.join(map(str,a)) if ok else '-1')
print('\n'.join(out))
