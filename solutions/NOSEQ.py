#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
for _ in range(next(it)):
 n=next(it);k=next(it);s=next(it);a=[];ok=True
 for i in range(n):
  r=s%k
  if r==0:v=0
  elif r==1:v=1
  elif r==k-1:v=-1
  else:ok=False;v=0
  a.append(v);s=(s-v)//k
 out.append(' '.join(map(str,a)) if ok and s==0 else '-2')
print('\n'.join(out))
