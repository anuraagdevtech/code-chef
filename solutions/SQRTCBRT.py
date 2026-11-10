#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
def cube(n):
 r=int(n**(1/3))
 while (r+1)**3<=n:r+=1
 while r**3>n:r-=1
 return r
for _ in range(next(it)):
 x=next(it);j=x
 while True:
  v=x+cube(j*j)
  if v==j:break
  j=v
 out.append(str(j*j))
print('\n'.join(out))
