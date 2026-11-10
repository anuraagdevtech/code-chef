#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 n=next(it);a=[str(next(it)) for _ in range(n)];answer=0
 for length in range(1,max(map(len,a))+1):
  vals=[s.zfill(length) for s in a if len(s)<=length]
  size=4**length;f=[0]*size
  for s in vals:
   ix=0;power=1
   for ch in reversed(s):
    d=int(ch)
    if d>7:break
    level=0 if d<=3 else 1 if d==4 else 2 if d<=6 else 3;ix+=level*power;power*=4
   else:f[ix]+=1
  power=1
  for _ in range(length):
   for base in range(0,size,power*4):
    for j in range(power):
     for digit in range(1,4):f[base+digit*power+j]+=f[base+(digit-1)*power+j]
   power*=4
  subtotal=0
  for ix,count in enumerate(f):
   sign=1;z=ix
   for _ in range(length):
    if z%4 in (0,2):sign=-sign
    z//=4
   subtotal+=sign*((1<<count)-1)
  answer+=subtotal
 # Each shorter lucky result was counted in its own length only: leading zero
 # must be excluded from the current length, since its thresholds use 4/7.
 out.append(str(answer))
print('\n'.join(out))
