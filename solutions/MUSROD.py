#!/usr/bin/env python3
import sys
it=iter(map(int,sys.stdin.buffer.read().split()))
out=[]
from functools import cmp_to_key
for _ in range(next(it)):
 n=next(it);a=[next(it) for _ in range(n)];b=[next(it) for _ in range(n)]
 rods=sorted(zip(a,b),key=cmp_to_key(lambda x,y:(x[1]*y[0]>y[1]*x[0])-(x[1]*y[0]<y[1]*x[0])))
 pos=ans=0
 for length,beauty in rods:ans+=pos*beauty;pos+=length
 out.append(str(ans))
print('\n'.join(out))
