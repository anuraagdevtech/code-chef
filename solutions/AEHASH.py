#!/usr/bin/env python3
import sys
from functools import lru_cache
p=1000000007
@lru_cache(None)
def distribution(n,a):
 if a<0 or a>n:return ()
 if n<=1:return (1,) if a==0 else (0,1)
 left=n//2;right=n-left;result=[0]*(a*(n.bit_length()+1)+1)
 for x in range(max(0,a-right),min(a,left)+1):
  f=distribution(left,x);g=distribution(right,a-x);sf=sg=0
  for v in range(max(len(f),len(g))):
   fv=f[v] if v<len(f) else 0;gv=g[v] if v<len(g) else 0;sg=(sg+gv)%p
   result[a+v]=(result[a+v]+fv*sg+gv*sf)%p;sf=(sf+fv)%p
 while result and result[-1]==0:result.pop()
 return tuple(result)
it=iter(map(int,sys.stdin.buffer.read().split()));out=[]
for _ in range(next(it)):
 a,e,v=next(it),next(it),next(it);d=distribution(a+e,a);out.append(str(d[v] if v<len(d) else 0))
print('\n'.join(out))
