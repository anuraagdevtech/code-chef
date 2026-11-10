#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 n=int(next(it));s=next(it);dp=list(range(n+1));pal=bytearray(n)
 for r in range(n):
  best=r+1
  for l in range(r+1):
   pal[l]=s[l]==s[r] and (r-l<2 or pal[l+1])
   if pal[l]:best=min(best,dp[l]+1)
  dp[r+1]=best
 out.append(str(dp[n]))
print('\n'.join(out))
