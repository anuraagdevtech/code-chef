#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);k=next(it);ranges=[(next(it),next(it)) for _ in range(n)];d=[0]*100002
 for l,r in ranges:d[l]+=1;d[r+1]-=1
 cur=basecount=0;p=[0]*100001
 for i in range(1,100001):
  cur+=d[i];basecount+=cur==k;p[i]=p[i-1]+(cur==k+1)-(cur==k)
 out.append(str(basecount+max(p[r]-p[l-1] for l,r in ranges)))
print('\n'.join(out))
