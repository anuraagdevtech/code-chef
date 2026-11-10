#!/usr/bin/env python3
import sys
from bisect import bisect_right
it=iter(map(int,sys.stdin.buffer.read().split()));n,m=next(it),next(it);a=[next(it) for _ in range(n)];dp=[0]*n;prefix=[0,1];left=0;p=1000000007
for i in range(1,n):
 while left<i and a[i]-a[left]>m:left+=1
 if left==i:print('-1 0');sys.exit()
 dp[i]=dp[left]+1;r=bisect_right(dp,dp[left],left,i);ways=(prefix[r]-prefix[left])%p;prefix.append((prefix[-1]+ways)%p)
print(dp[-1]-1,(prefix[-1]-prefix[-2])%p)
