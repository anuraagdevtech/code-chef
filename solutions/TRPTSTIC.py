#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from array import array
for _ in range(next(it)):
 n=next(it);m=next(it);k=next(it)+1;a=[next(it) for _ in range(n*m)];stride=m+1
 p=array('q',[0])*((n+1)*stride)
 for i in range(n):
  cur=0;row=(i+1)*stride;prev=i*stride
  for j in range(m):cur+=a[i*m+j];p[row+j+1]=p[prev+j+1]+cur
 if p[-1]<k:out.append('-1');continue
 def possible(d):
  for i in range(n):
   top=max(0,i-d)*stride;bot=min(n,i+d+1)*stride
   for j in range(m):
    if a[i*m+j]:
     l=max(0,j-d);r=min(m,j+d+1)
     if p[bot+r]-p[top+r]-p[bot+l]+p[top+l]>=k:return True
  return False
 lo=0;hi=max(n,m)-1
 while lo<hi:
  mid=(lo+hi)//2
  if possible(mid):hi=mid
  else:lo=mid+1
 out.append(str(lo))
print('\n'.join(out))
