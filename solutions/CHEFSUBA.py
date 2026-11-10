#!/usr/bin/env python3
import sys
from collections import deque
it=iter(sys.stdin.buffer.read().split());n,k,q=(int(next(it)) for _ in range(3));k=min(k,n);a=[int(next(it)) for _ in range(n)];s=next(it);a+=a;pref=[0]
for x in a:pref.append(pref[-1]+x)
w=[pref[i+k]-pref[i] for i in range(2*n-k+1)];width=n-k+1;d=deque();ans=[]
for i,x in enumerate(w):
 while d and w[d[-1]]<=x:d.pop()
 d.append(i)
 while d[0]<=i-width:d.popleft()
 if i>=width-1:ans.append(w[d[0]])
start=0;out=[]
for ch in s:
 if ch==33:start=(start-1)%n
 else:out.append(str(ans[start]))
print('\n'.join(out))
