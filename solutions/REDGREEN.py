#!/usr/bin/env python3
"""REDGREEN: standalone Python 3 solution."""
import sys
P=998244353
fac=[1]*200001
for i in range(1,200001):fac[i]=fac[i-1]*i%P
inv=[1]*200001;inv[-1]=pow(fac[-1],P-2,P)
for i in range(200000,0,-1):inv[i-1]=inv[i]*i%P
def solve(it):
 n,m=next(it),next(it);p=998244353;k=n+m-1
 if k&1:return '0'
 def comb(a,b):return fac[a]*inv[b]%p*inv[a-b]%p
 return str(comb(n+m-2,n-1)*comb(k,k//2)%p*pow(2,n*m-k,p)%p)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
