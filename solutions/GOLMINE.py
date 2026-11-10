#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);chef=0.;total=0
 for _ in range(n):
  g=next(it);a=next(it);b=next(it);chef+=g*b/(a+b);total+=g
 out.append(f'{chef:.10f} {total-chef:.10f}')
print('\n'.join(out))
