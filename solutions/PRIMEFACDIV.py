#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from math import gcd
for _ in range(next(it)):
 a=next(it);b=next(it)
 while b>1:
  g=gcd(a,b)
  if g==1:break
  b//=g
 out.append('YES' if b==1 else 'NO')
print('\n'.join(out))
