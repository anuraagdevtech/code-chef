#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
cases=[];mx=0
for _ in range(next(it)):
 n=next(it);k=next(it);odd=sum(next(it)%2 for _ in range(n));cases.append((n,k,odd));mx=max(mx,n)
f=[1]*(mx+1);mod=10**9+7
for i in range(1,mx+1):f[i]=f[i-1]*i%mod
for n,k,o in cases:
 if n==1:ans=1
 elif k==0:ans=f[n] if o==0 or o==n else 0
 else:ans=f[o]*f[n-o]*((o==(n+1)//2)+(o==n//2))%mod
 out.append(str(ans))
print('\n'.join(out))
