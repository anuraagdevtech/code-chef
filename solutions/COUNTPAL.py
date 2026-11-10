#!/usr/bin/env python3
import sys
s=sys.stdin.buffer.read().strip();n=len(s);dp=[0]*(n+1);dp[0]=1;pal=bytearray(n)
for r in range(n):
 for l in range(r+1):
  pal[l]=s[l]==s[r] and (r-l<2 or pal[l+1])
  if pal[l]:dp[r+1]=(dp[r+1]+dp[l])%1000000007
print(dp[n])
