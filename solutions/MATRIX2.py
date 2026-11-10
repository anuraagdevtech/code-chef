#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());n,m=int(next(it)),int(next(it));a=[next(it) for _ in range(n)];below=[0]*(m+1);ans=0
for row in reversed(a):
 cur=[0]*(m+1);run=0
 for j in range(m-1,-1,-1):
  run=run+1 if row[j]==49 else 0;cur[j]=min(run,below[j+1]+1);ans+=cur[j]
 below=cur
print(ans)
