#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 x=next(it);y=next(it);ans=-1
 if y%x==0:
  z=y//x
  for k in range(1,61):
   s=z+k
   if s%2==0 and s.bit_count()==k:
    ans=sum(i for i in range(1,s.bit_length()) if (s>>i)&1)+k-1;break
 out.append(str(ans))
print('\n'.join(out))
