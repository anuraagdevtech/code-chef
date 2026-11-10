#!/usr/bin/env python3
"""TWOAVG: standalone Python 3 solution."""
import sys
def solve(it):
 n,m,k=next(it),next(it),next(it);a=sum(next(it) for _ in range(n));b=sum(next(it) for _ in range(m))
 if k==1:return '-1'
 def ok(z):
  # Put x copies of K in A and z-x copies of 1 in B.
  v=k*(m+z)-a-b-z+n;den=2*(k-1);x=v//den
  for t in (0,z,max(0,min(z,x)),max(0,min(z,x+1))):
   if (a+k*t)*(m+z-t)>(b+z-t)*(n+t):return True
  return False
 lo=-1;hi=1
 while not ok(hi):hi*=2
 while hi-lo>1:
  mid=(hi+lo)//2
  if ok(mid):hi=mid
  else:lo=mid
 return str(hi)

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
