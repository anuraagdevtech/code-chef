#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);a=[0]*n
 for _ in range(n):x=next(it)-1;y=next(it);a[x]=y
 ok=True;upper=lower=False
 for i,v in enumerate(a):
  if i==0 or abs(v-a[i-1])!=1:upper=lower=False
  upper=upper or i==0 or v==n
  lower=lower or i==n-1 or v==1
  if upper and lower:ok=False
 out.append('YES' if ok else 'NO')
print('\n'.join(out))
