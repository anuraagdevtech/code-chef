#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n,k=next(it),next(it);dp=[1]*(n+1)
 for i in range(k,n+1):dp[i]=(dp[i-1]+dp[i-k])%1000000007
 out.append(str(dp[n]))
print('\n'.join(out))
