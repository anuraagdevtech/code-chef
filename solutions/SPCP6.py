#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
qs=[next(it) for _ in range(next(it))];m=max(qs);mod=10**9+7
a=[0]*(m+1);b=[0]*(m+1);a[0]=1
for i in range(1,m+1):
 a[i]=(b[i-1]+sum(a[max(0,i-4):max(0,i-1)]))%mod
 b[i]=(a[i-1]+sum(b[max(0,i-4):max(0,i-1)]))%mod
for l in qs:out.append(str(sum(a[max(0,l-4):l])%mod))
print('\n'.join(out))
