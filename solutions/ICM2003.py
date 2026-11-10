#!/usr/bin/env python3
import sys,math
it=iter(map(float,sys.stdin.buffer.read().split()));t=int(next(it));out=[]
for _ in range(t):
 b=next(it);c=next(it);lo=0.;hi=math.pi/2
 for _ in range(55):
  x=(lo+hi)/2
  if (2*x+b)*math.sin(x)-(x*x+b*x+c)*math.cos(x)<0:lo=x
  else:hi=x
 x=(lo+hi)/2;out.append(f'{(x*x+b*x+c)/math.sin(x):.10f}')
print('\n'.join(out))
