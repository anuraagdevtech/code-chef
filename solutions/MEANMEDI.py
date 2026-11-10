#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n,k=next(it),next(it);a=sorted(next(it) for _ in range(n));lc=(k-1)//2;rc=k//2;dp=[1]+[0]*max(lc,rc);left=[]
 for x in a:
  left.append(dp[lc])
  for j in range(lc,0,-1):dp[j]|=dp[j-1]<<x
 dp=[1]+[0]*rc;right=[0]*n
 for i in range(n-1,-1,-1):
  right[i]=dp[rc]
  for j in range(rc,0,-1):dp[j]|=dp[j-1]<<a[i]
 best=10**9
 for i in range(lc,n-rc):
  l=left[i];r=right[i];target=a[i]*(k-1)
  while l:
   bit=l&-l;s=bit.bit_length()-1;l-=bit;t=target-s
   if t<0:distance=s+(r&-r).bit_length()-1-target
   else:
    lower=r&((1<<(t+1))-1);distance=abs((lower.bit_length()-1)-t) if lower else 10**9
    upper=r>>t
    if upper:distance=min(distance,(upper&-upper).bit_length()-1)
   best=min(best,distance)
   if best==0:break
  if best==0:break
 out.append('%.3f'%(best/k))
print('\n'.join(out))
