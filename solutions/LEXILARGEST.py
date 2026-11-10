#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from math import gcd
for _ in range(next(it)):
 n=next(it);m=next(it);a=[next(it) for _ in range(n)];b=[a[0]]
 for i in range(1,n):
  r=a[i-1]//a[i];v=m//a[i]
  while gcd(v,r)!=1:v-=1
  b.append(a[i]*v)
 out.append(' '.join(map(str,b)))
print('\n'.join(out))
