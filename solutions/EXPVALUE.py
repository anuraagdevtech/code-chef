#!/usr/bin/env python3
import sys
n,p=map(int,sys.stdin.buffer.read().split());mod=998244353;inv=pow(p,-1,mod);half=(mod+1)//2
mean=second=0;w=1;out=[]
for i in range(n):
 second=(second+mean*w+half*w*w)%mod;mean=(mean+half*w)%mod;out.append(str(second));w=w*inv%mod
print(' '.join(out))
