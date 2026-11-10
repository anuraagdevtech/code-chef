#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];pos=[0]*(n+1)
 for i,v in enumerate(a):pos[v]=i
 lo=hi=pos[n];ans=1
 for v in range(n-1,1,-1):
  lo=min(lo,pos[v]);hi=max(hi,pos[v])
  if hi-lo+1==n-v+1:ans=n-v+1
 out.append(str(ans))
print('\n'.join(out))
