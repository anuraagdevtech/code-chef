#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from math import isqrt
cases=[(next(it),next(it)) for _ in range(next(it))];mod=10**9+7;mx=50000
f=[1]*(mx+1)
for i in range(1,mx+1):f[i]=f[i-1]*i%mod
iv=[1]*(mx+1);iv[mx]=pow(f[mx],-1,mod)
for i in range(mx,0,-1):iv[i-1]=iv[i]*i%mod
def cell(x):
 r=(isqrt(8*x-7)+1)//2
 if r*(r+1)//2<x:r+=1
 return r,x-r*(r-1)//2
for s,e in cases:
 r,c=cell(s);u,v=cell(e);d=u-r;k=v-c
 out.append(str(f[d]*iv[k]%mod*iv[d-k]%mod) if 0<=k<=d else '0')
print('\n'.join(out))
