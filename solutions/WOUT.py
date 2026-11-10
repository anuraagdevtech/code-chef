#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n,h=next(it),next(it);d=[0]*(n+1)
 for _ in range(n):l,r=next(it),next(it);d[l]+=1;d[r+1]-=1
 active=0
 for i in range(n):active+=d[i];d[i]=active
 s=sum(d[:h]);best=s
 for i in range(h,n):s+=d[i]-d[i-h];best=max(best,s)
 out.append(str(n*h-best))
print('\n'.join(out))
