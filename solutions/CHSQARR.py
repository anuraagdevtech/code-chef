#!/usr/bin/env python3
import sys
from collections import deque
it=iter(map(int,sys.stdin.buffer.read().split()));n,m=next(it),next(it);a=[[next(it) for _ in range(m)] for _ in range(n)];prefix=[[0]*(m+1) for _ in range(n+1)]
for i in range(n):
 total=0
 for j in range(m):total+=a[i][j];prefix[i+1][j+1]=prefix[i][j+1]+total
out=[];cache={}
for _ in range(next(it)):
 h,w=next(it),next(it)
 if (h,w) not in cache:
  horizontal=[]
  for row in a:
   q=deque();r=[]
   for j,x in enumerate(row):
    while q and row[q[-1]]<=x:q.pop()
    q.append(j)
    while q[0]<=j-w:q.popleft()
    if j>=w-1:r.append(row[q[0]])
   horizontal.append(r)
  best=10**30
  for j in range(m-w+1):
   q=deque()
   for i in range(n):
    x=horizontal[i][j]
    while q and horizontal[q[-1]][j]<=x:q.pop()
    q.append(i)
    while q[0]<=i-h:q.popleft()
    if i>=h-1:
     top=i-h+1;total=prefix[i+1][j+w]-prefix[top][j+w]-prefix[i+1][j]+prefix[top][j];best=min(best,h*w*horizontal[q[0]][j]-total)
  cache[h,w]=best
 out.append(str(cache[h,w]))
print('\n'.join(out))
