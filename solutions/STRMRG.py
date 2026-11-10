#!/usr/bin/env python3
import sys
it=iter(sys.stdin.buffer.read().split());out=[]
for _ in range(int(next(it))):
 next(it);next(it);a=next(it);b=next(it);a=bytes(x for i,x in enumerate(a) if i==0 or x!=a[i-1]);b=bytes(x for i,x in enumerate(b) if i==0 or x!=b[i-1]);dp=[0]*(len(b)+1)
 for x in a:
  diag=0
  for j,y in enumerate(b,1):
   old=dp[j];dp[j]=diag+1 if x==y else max(dp[j],dp[j-1]);diag=old
 out.append(str(len(a)+len(b)-dp[-1]))
print('\n'.join(out))
