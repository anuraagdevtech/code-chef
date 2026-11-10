#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];candidates={0,1,n-1}
 if n>2:
  d=a[1]-a[0]
  for i in range(2,n):
   if a[i]-a[i-1]!=d:candidates.update((i-1,i));break
 valid=[]
 for skip in candidates:
  b=[x for i,x in enumerate(a) if i!=skip]
  if len(b)<3 or all(b[i]-b[i-1]==b[1]-b[0] for i in range(2,len(b))):valid.append(a[skip])
 out.append(str(min(valid,default=-1)))
print('\n'.join(out))
