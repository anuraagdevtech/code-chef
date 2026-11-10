#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);k=next(it);h=n//2;low=3*h;high=199999*h
 if k<low or k>high or (k-low)%2:out.append('-1');continue
 a=[1]*h+[2]*h;r=(k-low)//2
 for i in range(n):v=min(r,49999);a[i]+=2*v;r-=v
 out.append(' '.join(map(str,a)))
print('\n'.join(out))
