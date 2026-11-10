#!/usr/bin/env python3
"""DIANE: standalone Python 3 solution."""
import sys
def solve(it):
 d=next(it); q,r=divmod(d,99998); a=[]
 if q:a=[99999]*q+[100000]
 if r:
  if a:a.append(1)
  a.extend([r+1,r+2])
 if not a:a=[1]
 return str(len(a))+'\n'+' '.join(map(str,a))

if __name__ == '__main__':
 it=iter(map(int,sys.stdin.buffer.read().split()))
 t=int(next(it));out=[solve(it) for _ in range(t)]
 sys.stdout.write("\n".join(out))
