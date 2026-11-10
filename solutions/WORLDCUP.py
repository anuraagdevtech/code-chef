#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));cases=[(next(it),next(it),next(it)) for _ in range(next(it))];p=1000000007;mx=max((b for r,b,l in cases),default=0);f=[1]*(mx+1)
for i in range(1,mx+1):f[i]=f[i-1]*i%p
inv=[1]*(mx+1);inv[mx]=pow(f[mx],p-2,p)
for i in range(mx,0,-1):inv[i-1]=inv[i]*i%p
zero=[[0]*10 for _ in range(mx+1)]
for n in range(mx+1):
 s=0
 for l in range(10):
  if l<=n:s=(s+f[n]*inv[l]%p*inv[n-l])%p
  zero[n][l]=s
out=[]
for r,b,l in cases:
 ans=0
 if r%2==0 and r<=6*b:
  for six in range(min(b,r//6)+1):
   left=r-6*six
   if left%4:continue
   four=left//4;n=b-six-four
   if n>=0:ans=(ans+f[b]*inv[six]%p*inv[four]%p*inv[n]%p*zero[n][l])%p
 out.append(str(ans))
print('\n'.join(out))
