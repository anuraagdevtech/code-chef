#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it)
 if n<3:out.append('-1')
 elif n%3==0:out.append(f'{n//3} {n//3} {n//3}')
 elif n%2:out.append(f'1 1 {(n-1)//2}')
 else:
  p=n&-n;m=n//p
  out.append('-1' if m==1 else f'{p} {p} {p*((m-1)//2)}')
print('\n'.join(out))
