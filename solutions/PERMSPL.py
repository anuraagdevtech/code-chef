#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];d=[0]*n
 for i in range(n):
  for j in range(i):
   if a[j]>a[i]: d[i]+=1;d[j]+=1
 bits=1
 for x in d:bits|=bits<<x
 out.append('YES' if bits>>(sum(d)//2)&1 else 'NO')
print('\n'.join(out))
