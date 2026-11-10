#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[];mod=7051954
for _ in range(int(next(it))):
 n,l,a,b=(int(next(it)) for _ in range(4));s=next(it);low=max(0,a-n);high=min(l,a+n);dp=[0]*(high-low+1);dp[a-low]=1;last={}
 for ch in s:
  step=1 if ch==43 else -1;add=[0]*len(dp)
  if step==1:
   for j in range(1,len(dp)):add[j]=dp[j-1]
  else:
   for j in range(len(dp)-1):add[j]=dp[j+1]
  old=last.get(ch)
  for j in range(len(dp)):dp[j]=(dp[j]+add[j]-(old[j] if old else 0))%mod
  last[ch]=add
 out.append(str(dp[b-low] if low<=b<=high else 0))
print('\n'.join(out))
