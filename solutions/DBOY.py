#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n=next(it);h=[2*next(it) for _ in range(n)];coins=set(next(it) for _ in range(n));m=max(h);dp=[0]+[10**9]*m
 for x in range(1,m+1):dp[x]=1+min((dp[x-c] for c in coins if c<=x),default=10**9)
 out.append(str(sum(dp[x] for x in h)))
print('\n'.join(out))
