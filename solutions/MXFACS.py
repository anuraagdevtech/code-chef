#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it); best=0; ans=n; p=2
 while p*p<=n:
  e=0
  while n%p==0: n//=p; e+=1
  if e>best: best=e; ans=p
  p=3 if p==2 else p+2
 if best==0: ans=n
 out.append(str(ans))
print('\n'.join(out))
