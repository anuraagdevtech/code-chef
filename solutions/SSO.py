#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);counts=[0]*48
 for _ in range(n):
  x=next(it)
  while x:
   bit=x&-x;counts[bit.bit_length()-1]+=1;x-=bit
 ans=0
 for i in range(47):
  if counts[i]:ans|=1<<i
  counts[i+1]+=counts[i]//2
 out.append(str(ans))
print('\n'.join(out))
