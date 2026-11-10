#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 r=next(it);c=next(it);x=next(it);a=[[next(it) for _ in range(c)] for _ in range(r)]
 for i in range(r):
  for j in range(c):a[i][j]-=next(it)
 for row in a:
  diff=[0]*(c+1);cur=0
  for j in range(c):
   cur+=diff[j];v=row[j]+cur
   if j+x<=c:cur-=v;diff[j+x]+=v;row[j]=0
   else:row[j]=v
 ok=True
 for j in range(c-x+1,c):
  diff=[0]*(r+1);cur=0
  for i in range(r):
   cur+=diff[i];v=a[i][j]+cur
   if i+x<=r:cur-=v;diff[i+x]+=v
   elif v:ok=False
 out.append('YES' if ok else 'NO')
print('\n'.join(out))
