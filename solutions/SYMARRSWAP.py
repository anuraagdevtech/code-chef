#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];b=[next(it) for _ in range(n)]
 items=sorted([(v,i) for i,v in enumerate(a)]+[(v,i) for i,v in enumerate(b)])
 counts=[0]*n;have=0;l=0;ans=10**18
 for r,(v,i) in enumerate(items):
  if counts[i]==0:have+=1
  counts[i]+=1
  while have==n:
   ans=min(ans,v-items[l][0]);j=items[l][1];counts[j]-=1;l+=1
   if counts[j]==0:have-=1
 out.append(str(ans))
print('\n'.join(out))
