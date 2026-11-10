#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
n=next(it);k=next(it);a=[next(it) for _ in range(n)];limit=max(a);divisors=[[] for _ in range(max(1,limit-k+1))]
for d in range(k+1,limit-k+1):
 for v in range(d,limit-k+1,d):divisors[v].append(d)
last=[-1]*(limit+1);special=-1;left=0;ans=0
for i,x in enumerate(a):
 if x>k:left=max(left,last[x]+1,special+1)
 ans+=i-left+1
 if x==k:special=i
 elif x>k:
  for d in divisors[x-k]:last[d]=i
print(ans)
