#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);q=next(it);a=[0]*(n+2);b=[0]*(n+2)
 for _ in range(q):
  l=next(it);r=next(it);a[l]+=1;a[r+1]-=1;b[l]+=1-l;b[r+1]-=1-l
 x=y=0;row=[]
 for i in range(1,n+1):x+=a[i];y+=b[i];row.append(str(x*i+y))
 out.append(' '.join(row))
print('\n'.join(out))
