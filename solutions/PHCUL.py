#!/usr/bin/env python3
import sys
from math import hypot
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 x,y=next(it),next(it);n,m,k=next(it),next(it),next(it);a=[(next(it),next(it)) for _ in range(n)];b=[(next(it),next(it)) for _ in range(m)];c=[(next(it),next(it)) for _ in range(k)]
 da=[hypot(u-x,v-y) for u,v in a];db=[hypot(u-x,v-y) for u,v in b];ea=[min(hypot(u-r,v-s) for r,s in c) for u,v in a];eb=[min(hypot(u-r,v-s) for r,s in c) for u,v in b];ans=float('inf')
 for i,(u,v) in enumerate(a):
  for j,(r,s) in enumerate(b):ans=min(ans,hypot(u-r,v-s)+min(da[i]+eb[j],db[j]+ea[i]))
 out.append('%.10f'%ans)
print('\n'.join(out))
