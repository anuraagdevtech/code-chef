#!/usr/bin/env python3
"""TDISTS: standalone Python 3 solution."""
import sys
from math import isqrt

def solve(it):
 x,y=next(it),next(it);n=isqrt(x+y);z=isqrt(max(0,x-y))
 if n*n!=x+y or x<y or z*z!=x-y or (n-z)%2:return 'NO'
 a=(n+z)//2;b=n-a
 if b==0:return 'NO'
 edges=['1 '+str(i) for i in range(a+1,n+1)]+[str(a+1)+' '+str(i) for i in range(2,a+1)]
 return 'YES\n'+str(n)+'\n'+'\n'.join(edges)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
