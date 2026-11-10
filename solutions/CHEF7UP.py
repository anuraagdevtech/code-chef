#!/usr/bin/env python3
"""CHEF7UP: standalone Python 3 solution."""
import sys
from bisect import bisect_left

def solve(it):
 n,c=next(it),next(it);p=sorted(next(it) for _ in range(n));mid=bisect_left(p,c);ans=0
 for i in range(mid-1,-1,-1):
  if (p[i]-c)%2==0:break
  ans+=1
 for i in range(mid,n):
  if (p[i]-c)%2==0:break
  ans+=1
 return str(ans)+' '+('1' if ans==n else '-1')

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
