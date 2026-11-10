#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));n=next(it);a=[next(it) for _ in range(n)];out=[]
for _ in range(next(it)):
 k=next(it);values=[]
 for x in a:
  t=next(it)
  if t:values.append(t*x)
 if k>len(values):out.append('0');continue
 if k==1:out.append(str(sum(values)));continue
 pref=[0]
 for x in values:pref.append(pref[-1]+x)
 m=len(values);ans=0
 for bit in range(pref[-1].bit_length()-1,-1,-1):
  mask=ans|1<<bit;dp=[0]*(m+1);dp[0]=1
  for r in range(1,m+1):
   possibilities=0
   for l in range(r):
    if (pref[r]-pref[l])&mask==mask:possibilities|=dp[l]<<1
   dp[r]=possibilities
  if dp[m]>>k&1:ans=mask
 out.append(str(ans))
print('\n'.join(out))
