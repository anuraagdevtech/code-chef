#!/usr/bin/env python3
import sys
from collections import deque
it=iter(sys.stdin.buffer.read().split());n,q,k=(int(next(it)) for _ in range(3));a=[int(next(it)) for _ in range(n)];s=next(it);a+=a;starts=[0]*len(a);run=0
for i,x in enumerate(a):run=run+1 if x else 0;starts[i]=i-run+1
# For window [l,l+n), max run is max of clipped ending runs.
d=deque();ans=[]
for i,x in enumerate(a):
 length=i-starts[i]+1 if x else 0
 while d and d[-1][1]<=length:d.pop()
 d.append((i,length))
 left=i-n+1
 while d and d[0][0]<left:d.popleft()
 if left>=0:
  # The longest uncut run may start before the window. Since run lengths
  # strictly decrease in deque order, only the first such run can be clipped.
  while len(d)>1 and min(d[0][1],d[0][0]-left+1)<=d[1][1]:d.popleft()
  ans.append(min(k,d[0][1],d[0][0]-left+1))
start=0;out=[]
for ch in s:
 if ch==33:start=(start-1)%n
 else:out.append(str(ans[start]))
print('\n'.join(out))
